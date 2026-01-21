#!/usr/bin/env python3
"""
Static Wiki Builder with Tyrian Theme
Converts markdown files to static HTML using Mustache templates
Supports nested folder structure with automatic navigation generation
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

# Import custom Gentoo extension
sys.path.insert(0, str(Path(__file__).parent))
from gentoo_extension import GentooExtension


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

        # Now using content/ as root, not content/wiki
        self.content_dir = self.project_root / 'content'
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
                'markdown.extensions.fenced_code',
                GentooExtension()
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

        # Navigation structure (built from content folder)
        self.navigation = None

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
            'show_search': True
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

        # Copy custom CSS
        custom_css_src = self.project_root / 'assets' / 'css' / 'custom.css'
        if custom_css_src.exists():
            css_dir = self.assets_dest / 'css'
            css_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(custom_css_src, css_dir / 'custom.css')

        # Copy favicon if exists
        favicon_src = self.project_root / 'favicon.ico'
        if favicon_src.exists():
            shutil.copy2(favicon_src, self.output_dir / 'favicon.ico')

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

    def build_navigation(self):
        """Build navigation structure from content folder

        Returns:
            list: Navigation structure with nested items
        """
        self.log('Building navigation from content structure...')

        if not self.content_dir.exists():
            return []

        nav_items = []
        base_url = self.config.get('base_url', '')

        # Get all directories in content (these are top-level nav items)
        for item in sorted(self.content_dir.iterdir()):
            if not item.is_dir():
                # If it's README.md at root, it's the Main Page
                if item.name.lower() == 'readme.md':
                    nav_items.append({
                        'title': 'Main page',
                        'url': f'{base_url}/',
                        'children': []
                    })
                continue

            # Get the README.md in this directory for the title/link
            readme_file = item / 'README.md'
            if readme_file.exists():
                try:
                    metadata, _ = self.extract_metadata(readme_file)
                    title = metadata.get('title', item.name.replace('-', ' ').replace('_', ' ').title())
                except:
                    title = item.name.replace('-', ' ').replace('_', ' ').title()

                # Build URL path
                rel_path = item.relative_to(self.content_dir)
                url = f'{base_url}/{"/".join(rel_path.parts)}/'

                # Build children (subdirectories)
                children = self._build_nav_children(item, base_url, rel_path)

                nav_items.append({
                    'title': title,
                    'url': url,
                    'children': children
                })

        self.navigation = nav_items

        # Also build HTML version for template
        self.navigation_html = self._render_navigation_html(nav_items)

        return nav_items

    def _render_navigation_html(self, nav_items):
        """Render navigation items to HTML

        Args:
            nav_items: List of navigation items

        Returns:
            str: HTML string for navigation
        """
        html = ''

        for item in nav_items:
            if item.get('children'):
                # Has children - make a dropdown
                html += f'''<li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button">{item['title']} <span class="caret"></span></a>
                    <ul class="dropdown-menu" role="menu">
                        <li><a href="{item['url']}">{item['title']}</a></li>
                        <li class="divider"></li>
                        {self._render_nested_nav_html(item['children'])}
                    </ul>
                </li>'''
            else:
                # No children - simple link
                active_class = ' class="active"' if item.get('is_active') else ''
                html += f'<li{active_class}><a href="{item["url"]}" title="{item["title"]}">{item["title"]}</a></li>'

        return html

    def _render_nested_nav_html(self, nav_items, depth=0):
        """Render nested navigation items to HTML

        Args:
            nav_items: List of navigation items
            depth: Current depth (for styling)

        Returns:
            str: HTML string for nested navigation
        """
        html = ''

        for item in nav_items:
            if item.get('children'):
                # Nested dropdown
                html += f'''<li class="dropdown{'-submenu' if depth > 0 else ''}">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button">{item['title']} <span class="caret"></span></a>
                    <ul class="dropdown-menu" role="menu">
                        <li><a href="{item['url']}">{item['title']}</a></li>
                        <li class="divider"></li>
                        {self._render_nested_nav_html(item['children'], depth + 1)}
                    </ul>
                </li>'''
            else:
                html += f'<li><a href="{item["url"]}">{item["title"]}</a></li>'

        return html

    def _build_nav_children(self, directory, base_url, parent_path):
        """Build navigation children for subdirectories

        Args:
            directory: Path to directory
            base_url: Base URL from config
            parent_path: Parent path for URL building

        Returns:
            list: Child navigation items
        """
        children = []

        # Sort directories first, then files
        items = sorted(directory.iterdir(), key=lambda x: (not x.is_dir(), x.name))

        for item in items:
            if item.is_dir():
                # Recursively build subdirectories
                readme_file = item / 'README.md'
                if readme_file.exists():
                    try:
                        metadata, _ = self.extract_metadata(readme_file)
                        title = metadata.get('title', item.name.replace('-', ' ').replace('_', ' ').title())
                    except:
                        title = item.name.replace('-', ' ').replace('_', ' ').title()

                    rel_path = item.relative_to(self.content_dir)
                    url = f'{base_url}/{"/".join(rel_path.parts)}/'

                    sub_children = self._build_nav_children(item, base_url, rel_path)

                    children.append({
                        'title': title,
                        'url': url,
                        'children': sub_children
                    })

        return children

    def get_breadcrumb(self, relative_path):
        """Generate breadcrumb from file path

        Args:
            relative_path: Relative path from content directory

        Returns:
            list: List of breadcrumb items
        """
        parts = Path(relative_path).parts[:-1]  # Exclude filename
        breadcrumb = []
        base_url = self.config.get('base_url', '')

        for i, part in enumerate(parts):
            url = f'{base_url}/' + '/'.join(parts[:i+1]) + '/'
            breadcrumb.append({
                'title': part.replace('-', ' ').replace('_', ' ').title(),
                'url': url
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

        # Generate breadcrumb
        breadcrumb = self.get_breadcrumb(relative_path)

        # Add table of contents to content if enabled
        toc_value = metadata.get('toc', 'true')
        show_toc = (toc_value == 'true' or toc_value is True) if not isinstance(toc_value, bool) else toc_value
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
            'content': html_content,
            'current_page': title,
            'breadcrumb': breadcrumb,
            'show_search': self.config.get('show_search', True),
            'site_domain': self.config.get('site_url', '').replace('https://', '').replace('http://', ''),
            'navigation_html': getattr(self, 'navigation_html', ''),
            'navigation': self.navigation if self.navigation else []
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
            self.log('Creating sample content...', 'INFO')
            self.create_sample_content()
            # Re-scan after creating sample content
            md_files = list(self.content_dir.rglob('*.md'))

        # Build navigation first
        self.build_navigation()

        for md_file in md_files:
            relative_path = md_file.relative_to(self.content_dir)

            # Determine output path
            # README.md -> index.html in that directory
            if md_file.name.lower() == 'readme.md':
                # README.md becomes index.html in its directory
                output_rel_path = relative_path.parent / 'index.html'
            else:
                # Other files keep their name but become .html
                output_rel_path = relative_path.with_suffix('.html')

            output_file = self.output_dir / output_rel_path

            self.generate_page(md_file, output_file)

        self.log(f'Processed {len(md_files)} files.')

    def create_sample_content(self):
        """Create sample wiki content"""
        self.content_dir.mkdir(parents=True, exist_ok=True)

        # Create sample README.md at root (Main Page)
        home_content = """---
title: Main Page
layout: wiki
description: Welcome to the static wiki
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
- 📂 Nested folder support
- 🔄 Git-based workflow

## Getting Started

This wiki system allows you to:

1. Write content in Markdown
2. Organize pages in nested directories
3. Add metadata with frontmatter
4. Build static HTML files
5. Deploy to GitHub Pages or any static hosting

## Navigation

The navigation is automatically generated from your folder structure:

- Create folders in `content/` to add navigation items
- Add `README.md` to a folder to define its title and content
- Nest folders to create dropdown menus
- Place `README.md` in the root for the main page

## Formatting

This wiki supports Gentoo-style formatting:

```cmd root
emerge --ask app-editors/vim
```

```file /etc/conf.d/hostname
# Set the hostname of the system
hostname="mygentoo"
```

```warning
Important
Always backup your data before making system changes!
```

Enjoy your new static wiki!
"""

        with open(self.content_dir / 'README.md', 'w', encoding='utf-8') as f:
            f.write(home_content)

        # Create sample Documentation folder
        docs_dir = self.content_dir / 'documentation'
        docs_dir.mkdir(exist_ok=True)

        docs_readme = """---
title: Documentation
layout: wiki
description: Documentation index
toc: true
---

# Documentation

Welcome to the documentation section.

## Getting Started

- [Installation Guide](installation.html)
- [Configuration Guide](configuration.html)
"""

        with open(docs_dir / 'README.md', 'w', encoding='utf-8') as f:
            f.write(docs_readme)

        # Create sample installation page
        install_content = """---
title: Installation Guide
layout: wiki
description: How to install and configure the wiki
toc: true
---

# Installation Guide

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Steps

1. Clone the repository
2. Install dependencies: `pip install markdown pystache python-frontmatter`
3. Build: `python scripts/markdown2html.py`

## Next Steps

See the [Configuration Guide](configuration.html) for more details.
"""

        with open(docs_dir / 'installation.md', 'w', encoding='utf-8') as f:
            f.write(install_content)

        # Create sample configuration page
        config_content = """---
title: Configuration Guide
layout: wiki
description: How to configure the wiki
toc: true
---

# Configuration Guide

## config.json

Edit `config.json` to customize your wiki:

```json
{
  "site_name": "My Wiki",
  "site_url": "https://example.com",
  "base_url": "",
  "site_description": "My documentation site"
}
```

## Content Structure

Create folders in `content/` to organize your pages:

```
content/
├── README.md           # Main page
├── documentation/      # Documentation section
│   ├── README.md
│   ├── installation.md
│   └── configuration.md
└── guides/             # Guides section
    └── README.md
```
"""

        with open(docs_dir / 'configuration.md', 'w', encoding='utf-8') as f:
            f.write(config_content)

        self.log('Sample content created.')

    def build(self):
        """Build the entire static site"""
        self.log('Starting static wiki build...')
        self.log(f'Project root: {self.project_root}')

        self.clean_output()
        self.copy_assets()
        self.process_all_files()

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
