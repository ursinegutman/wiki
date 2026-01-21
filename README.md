# Static Wiki with Tyrian Theme

A lightweight static wiki system powered by the beautiful **Tyrian theme** from Gentoo. Write your content in Markdown, build it into static HTML, and deploy anywhere - including GitHub Pages.

![Tyrian Theme](https://img.shields.io/badge/theme-Tyrian-purple)
![Markdown](https://img.shields.io/badge/markup-Markdown-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Features

- 🎨 **Beautiful Tyrian Theme** - The same theme used by Gentoo Wiki
- 📝 **Markdown Authoring** - Write content in familiar Markdown format
- 🚀 **Static Site Generation** - Fast, secure, and easy to deploy
- 📱 **Responsive Design** - Works perfectly on mobile, tablet, and desktop
- 🔍 **Search Integration** - Built-in search capabilities
- 📂 **Category Support** - Organize content into categories
- 🔄 **Git-Based Workflow** - Version control for your documentation
- 🌐 **GitHub Pages Ready** - Deploy with automatic GitHub Actions workflow
- 🎯 **Zero Runtime Dependencies** - Pure static HTML/CSS/JS
- ✨ **Gentoo Wiki Formatting** - Command boxes, file boxes, alerts, and more

## Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/static-wiki-tyrian.git
cd static-wiki-tyrian
```

2. Install Python dependencies:

```bash
pip install markdown pystache python-frontmatter
```

3. Build the wiki:

```bash
python scripts/markdown2html.py
```

4. Preview locally:

```bash
cd output
python -m http.server 8000
```

Visit http://localhost:8000

## Project Structure

```
static-wiki-tyrian/
├── content/
│   └── wiki/              # Your markdown content
│       ├── index.md       # Home page
│       ├── formatting.md  # Formatting guide
│       └── *.md           # Other pages
├── templates/             # HTML templates with Tyrian theme
│   └── base.html
├── scripts/               # Build scripts
│   ├── build.sh          # Bash wrapper script
│   ├── markdown2html.py  # Python builder
│   └── gentoo_extension.py # Custom Markdown extensions
├── assets/
│   └── css/
│       └── custom.css    # Custom styles
├── output/               # Generated static HTML (auto-generated)
├── .github/
│   └── workflows/
│       └── deploy.yml    # GitHub Actions workflow
├── config.json           # Site configuration
└── README.md
```

## Creating Content

### Add a New Page

Create a markdown file in `content/wiki/`:

```markdown
---
title: My New Page
layout: wiki
description: A description of my page
toc: true
---

# My New Page

Content goes here in **Markdown** format.
```

### Frontmatter Options

- `title` - Page title (required)
- `layout` - Layout to use (default: "wiki")
- `description` - Page description for SEO
- `category` - Category for organization
- `toc` - Show table of contents (true/false)

## Gentoo Wiki Formatting

This wiki includes custom Markdown extensions that match Gentoo Wiki formatting:

### Command Boxes

Show terminal commands with colored prompts:

```cmd root
emerge --ask app-editors/vim
```

```cmd user
git clone https://github.com/ursinegutman/wiki.git
```

### File Boxes

Show configuration files with path and description:

```file /etc/conf.d/hostname
# Set the hostname of the system
hostname="mygentoo"
```

```file ~/.bashrc Sample bash configuration
export EDITOR=vim
```

### Alert Boxes

```warning
Important
Always backup your data before making system changes!
```

```success
Tip
The Gentoo Handbook is an excellent resource.
```

```info
Note
This wiki uses Markdown for content formatting.
```

```danger
Warning
Running commands as root can be dangerous!
```

### Standard Markdown

All standard Markdown features work:
- Headers: `# H1`, `## H2`, `### H3`
- Bold/Italic: `**bold**`, `*italic*`
- Links: `[text](url)`
- Code blocks: ` ```language `
- Tables, lists, blockquotes, and more

See [Formatting Guide](/formatting.html) for more examples.

## Configuration

Edit `config.json` to customize your wiki:

```json
{
  "site_name": "My Wiki",
  "site_url": "https://username.github.io/wiki",
  "base_url": "/wiki",
  "site_description": "My documentation site",
  "show_search": true,
  "categories": [
    {
      "name": "Documentation",
      "slug": "documentation"
    }
  ]
}
```

**Important**: For GitHub Pages, set `base_url` to your repository name (e.g., `/wiki`).

## Building

### Build Commands

```bash
# Build
python scripts/markdown2html.py

# Clean build (removes output directory first)
python scripts/markdown2html.py --clean

# Using the bash wrapper
./scripts/build.sh
./scripts/build.sh --clean
```

## Deployment

### GitHub Pages (Recommended)

1. Create a new GitHub repository
2. Update `config.json` with your repository URL and base_url
3. Push your code:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/username/repo.git
git push -u origin main
```

4. Enable GitHub Pages in repository settings:
   - Go to Settings → Pages
   - Source: GitHub Actions

5. The workflow will automatically build and deploy on push!

### Manual Deployment

The `output/` directory contains pure static HTML that can be deployed to:

- **Netlify** - Drag and drop the output folder
- **Vercel** - Connect your repository
- **AWS S3** - Upload to a public bucket
- **Cloudflare Pages** - Connect repository
- **Any web server** - Copy files to server root

## Customization

### Styling

Edit `assets/css/custom.css` to customize styles. The Tyrian theme CSS is loaded from jsDelivr CDN.

### Templates

Edit `templates/base.html` to modify the layout. The template uses Mustache syntax:

```html
{{title}}         <!-- Page title -->
{{{content}}}     <!-- Page content (unescaped) -->
{{site_name}}     <!-- Site name from config -->
{{base_url}}      <!-- Base URL from config -->
```

### Navigation

Edit the navigation section in `templates/base.html` to customize menu items.

## Troubleshooting

### Python Module Errors

```bash
pip install --upgrade markdown pystache python-frontmatter
```

### Build Fails

1. Check that markdown files have valid frontmatter
2. Verify `content/wiki/` directory exists
3. Ensure `config.json` is valid JSON
4. Check Python version: `python3 --version` (must be 3.7+)

### Styles Not Loading

- Verify CDN links in `templates/base.html` are correct
- Clear browser cache and rebuild
- Check `base_url` in `config.json` matches your deployment path

## Credits

- **Tyrian Theme** by [Gentoo](https://www.gentoo.org/)
- Bootstrap 3.3.7
- Font Awesome 4.7.0
- Python Markdown library
- Mustache templating

## License

This project is licensed under the MIT License.

The Tyrian theme is copyright by Gentoo Foundation.

---

**Built with ❤️ using [Tyrian Theme](https://www.gentoo.org/) from Gentoo**
