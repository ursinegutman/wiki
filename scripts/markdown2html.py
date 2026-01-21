#!/usr/bin/env python3
"""
Static Wiki Builder with Tyrian Theme
Converts markdown files to static HTML using Mustache templates
"""

import os
import sys
import json
import re
import shutil
from datetime import datetime
from pathlib import Path
import frontmatter
import markdown
from pystache import Renderer


class WikiBuilder:
    """Static site generator for wiki using Tyrian theme"""

    def __init__(self, project_root=None):
        """Initialize the wiki builder

        Args:
            project_root: Path to project root directory
        """
        if project_root is None:
            self.project_root = Path(__file__).parent.parent
        else:
            self.project_root = Path(project_root)

        self.content_dir = self.project_root / 'content' / 'wiki'
        self.template_dir = self.project_root / 'templates'
        self.output_dir = self.project_root / 'output'
        self.assets_source = Path(__file__).parent.parent / 'node_modules' / '@gentoo' / 'tyrian' / 'dist'
        self.assets_dest = self.output_dir / 'assets'

        # Load configuration
        self.config = self.load_config()

        # Setup markdown processor
        self.md = markdown.Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
                'markdown.extensions.meta',
                'markdown.extensions.admonition',
                'markdown.extensions.tables',
                'markdown.extensions.fenced_code'
            ],
            extension_configs={
                'codehilite': {
                    'linenums': False,
                    'css_class': 'highlight'
                },
                'toc': {
                    'permalink': True,
                    'toc_depth': 3
                }
            }
        )

        # Setup Mustache renderer
        self.renderer = Renderer()

    def log(self, message, level='INFO'):
        """Log a message with level

        Args:
            message: Message to log
            level: Log level (INFO, WARN, ERROR)
        """
        colors = {
            'INFO': '\033[0;32m',
            'WARN': '\033[1;33m',
            'ERROR': '\033[0;31m',
            'RESET': '\033[0m'
        }
        color = colors.get(level, colors['RESET'])
        print(f"{color}[{level}]{colors['RESET']} {message}")

    def load_config(self):
        """Load site configuration from config.json

        Returns:
            dict: Configuration dictionary
        """
        config_file = self.project_root / 'config.json'
        if config_file.exists():
            with open(config_file, 'r') as f:
                return json.load(f)
        else:
            return self.get_default_config()

    def get_default_config(self):
        """Get default site configuration

        Returns:
            dict: Default configuration
        """
        return {
            'site_name': 'Static Wiki',
            'site_url': 'https://example.com',
            'base_url': '',
            'site_description': 'A static wiki powered by Tyrian theme',
            'language': 'en',
            'author': 'Wiki Admin',
            'year': str(datetime.now().year),
            'show_search': True,
            'categories': []
        }

    def clean_output(self):
        """Clean the output directory"""
        self.log('Cleaning output directory...')
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.assets_dest.mkdir(parents=True, exist_ok=True)

    def copy_assets(self):
        """Copy Tyrian theme assets to output directory"""
        self.log('Copying Tyrian theme assets...')

        if not self.assets_source.exists():
            self.log(f'Warning: Assets source not found at {self.assets_source}', 'WARN')
            self.log('Skipping asset copy...', 'WARN')
            return

        # Copy all assets
        for item in self.assets_source.iterdir():
            dest = self.assets_dest / item.name
            if item.is_dir():
                if dest.exists():
                    shutil.rmtree(dest)
                shutil.copytree(item, dest)
            else:
                shutil.copy2(item, dest)

        self.log('Assets copied successfully.')

    def extract_metadata(self, file_path):
        """Extract metadata from markdown file

        Args:
            file_path: Path to markdown file

        Returns:
            tuple: (metadata dict, content string)
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            return post.metadata, post.content

    def convert_markdown(self, content, metadata):
        """Convert markdown content to HTML

        Args:
            content: Markdown content string
            metadata: Metadata dictionary

        Returns:
            tuple: (html_content, toc_html)
        """
        # Reset markdown processor state
        self.md.reset()

        # Convert to HTML
        html_content = self.md.convert(content)

        # Extract table of contents
        toc_html = self.md.toc if hasattr(self.md, 'toc') else ''

        return html_content, toc_html

    def get_breadcrumb(self, relative_path):
        """Generate breadcrumb from file path

        Args:
            relative_path: Relative path from content directory

        Returns:
            list: List of breadcrumb items
        """
        parts = Path(relative_path).parts[:-1]  # Exclude filename
        breadcrumb = []

        for i, part in enumerate(parts):
            url = '/'.join(parts[:i+1]) + '/index.html'
            breadcrumb.append({
                'title': part.replace('-', ' ').replace('_', ' ').title(),
                'url': '/' + url
            })

        return breadcrumb

    def render_template(self, template_name, context):
        """Render a Mustache template

        Args:
            template_name: Name of template file
            context: Template context dictionary

        Returns:
            str: Rendered HTML
        """
        template_path = self.template_dir / template_name
        if not template_path.exists():
            self.log(f'Template not found: {template_name}', 'ERROR')
            return ''

        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()

        return self.renderer.render(template_content, context)

    def generate_page(self, input_file, output_file):
        """Generate a single HTML page from markdown file

        Args:
            input_file: Path to input markdown file
            output_file: Path to output HTML file
        """
        relative_path = input_file.relative_to(self.content_dir)
        self.log(f'Processing: {relative_path}')

        # Extract metadata and content
        metadata, content = self.extract_metadata(input_file)

        # Convert markdown to HTML
        html_content, toc_html = self.convert_markdown(content, metadata)

        # Get page metadata with defaults
        title = metadata.get('title', 'Untitled')
        description = metadata.get('description', self.config.get('site_description', ''))
        date = metadata.get('date', datetime.now().strftime('%Y-%m-%d'))
        author = metadata.get('author', self.config.get('author', ''))
        layout = metadata.get('layout', 'wiki')
        category = metadata.get('category', '')

        # Generate breadcrumb
        breadcrumb = self.get_breadcrumb(relative_path)

        # Add table of contents to content if enabled
        show_toc = metadata.get('toc', 'true').lower() == 'true'
        if show_toc and toc_html and layout == 'wiki':
            toc_section = f'''
            <div class="wiki-toc">
                <h3>Table of Contents</h3>
                {toc_html}
            </div>
            '''
            html_content = toc_section + html_content

        # Add metadata section
        meta_html = ''
        if date or author:
            meta_parts = []
            if date:
                meta_parts.append(f'Published: {date}')
            if author:
                meta_parts.append(f'Author: {author}')
            meta_html = f'<div class="wiki-meta">{" | ".join(meta_parts)}</div>'

        html_content = meta_html + html_content

        # Prepare template context
        context = {
            'title': title,
            'description': description,
            'site_name': self.config.get('site_name', 'Static Wiki'),
            'site_url': self.config.get('site_url', ''),
            'base_url': self.config.get('base_url', ''),
            'year': self.config.get('year', str(datetime.now().year)),
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'author': author,
            'date': date,
            'category': category,
            'content': html_content,
            'current_page': title,
            'breadcrumb': breadcrumb,
            'show_search': self.config.get('show_search', True),
            'site_domain': self.config.get('site_url', '').replace('https://', '').replace('http://', ''),
            'categories': self.config.get('categories', []),
            'sidebar_sections': self.config.get('sidebar_sections', [])
        }

        # Render template
        template_name = metadata.get('template', 'base.html')
        html = self.render_template(template_name, context)

        # Write output file
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)

    def process_all_files(self):
        """Process all markdown files in content directory"""
        self.log('Processing markdown files...')

        if not self.content_dir.exists():
            self.log(f'Content directory not found: {self.content_dir}', 'WARN')
            self.log('Creating sample content...', 'INFO')
            self.create_sample_content()

        # Find all markdown files
        md_files = list(self.content_dir.rglob('*.md'))

        if not md_files:
            self.log('No markdown files found!', 'WARN')
            return

        for md_file in md_files:
            relative_path = md_file.relative_to(self.content_dir)
            output_file = self.output_dir / relative_path.with_suffix('.html')

            self.generate_page(md_file, output_file)

        self.log(f'Processed {len(md_files)} files.')

    def create_sample_content(self):
        """Create sample wiki content"""
        self.content_dir.mkdir(parents=True, exist_ok=True)

        # Create sample home page
        home_content = """---
title: Welcome to Static Wiki
layout: wiki
description: A static wiki powered by Tyrian theme
toc: true
---

# Welcome to Static Wiki

This is a **static wiki** built with the beautiful **Tyrian theme** from Gentoo.

## Features

- 🎨 Beautiful Tyrian theme from Gentoo
- 📝 Write content in Markdown
- 🚀 Fast static site generation
- 📱 Responsive design
- 🔍 Search integration
- 📂 Category support
- 🔄 Git-based workflow

## Getting Started

This wiki system allows you to:

1. Write content in Markdown
2. Organize pages in directories
3. Add metadata with frontmatter
4. Build static HTML files
5. Deploy to GitHub Pages or any static hosting

## Sample Content

Check out these sample pages:

- [Installation Guide](installation-guide.html)
- [Configuration](configuration.html)
- [Contributing](contributing.html)

## Code Examples

You can include code blocks with syntax highlighting:

```python
def hello_world():
    print("Hello, World!")
    return True
```

```bash
# Build the wiki
./scripts/build.sh
```

## Tables

| Feature | Status |
|---------|--------|
| Markdown support | ✅ |
| Tyrian theme | ✅ |
| Static HTML | ✅ |
| GitHub Pages | ✅ |

## Alerts

!!! note
    This is a note alert.

!!! warning
    This is a warning alert.

!!! tip
    This is a tip alert.

Enjoy your new static wiki!
"""

        with open(self.content_dir / 'index.md', 'w', encoding='utf-8') as f:
            f.write(home_content)

        self.log('Sample content created.')

    def generate_indexes(self):
        """Generate index pages for categories and main wiki index"""
        self.log('Generating index pages...')

        # Generate main wiki index
        # TODO: Implement full index generation

        self.log('Index generation complete.')

    def build(self):
        """Build the entire static site"""
        self.log('Starting static wiki build...')
        self.log(f'Project root: {self.project_root}')

        self.clean_output()
        self.copy_assets()
        self.process_all_files()
        self.generate_indexes()

        self.log(f'Build complete! Output directory: {self.output_dir}')
        self.log('You can now deploy the contents to GitHub Pages or any static hosting service.')


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description='Static Wiki Builder with Tyrian Theme')
    parser.add_argument('--project-root', help='Path to project root directory')
    parser.add_argument('--clean', action='store_true', help='Clean output directory before building')

    args = parser.parse_args()

    builder = WikiBuilder(project_root=args.project_root)

    if args.clean:
        builder.clean_output()

    builder.build()


if __name__ == '__main__':
    main()
