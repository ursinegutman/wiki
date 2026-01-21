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
- 🎯 **Zero Dependencies Runtime** - Pure static HTML/CSS/JS

## Quick Start

### Prerequisites

- Node.js v14 or higher
- Python 3.7 or higher
- Git

### Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/static-wiki-tyrian.git
cd static-wiki-tyrian
```

2. Install dependencies:

```bash
# Install Python dependencies
pip install markdown pystache python-frontmatter

# Install Tyrian theme
npm install git+https://anongit.gentoo.org/git/sites/tyrian-theme.git
```

3. Build the wiki:

```bash
./scripts/build.sh
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
│       ├── getting-started.md
│       └── installation.md
├── templates/             # HTML templates with Tyrian theme
│   └── base.html
├── scripts/               # Build and deployment scripts
│   ├── build.sh          # Build script
│   ├── deploy.sh         # Deployment script
│   └── markdown2html.py  # Python builder
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
date: 2026-01-20
author: Your Name
category: Documentation
toc: true
---

# My New Page

Content goes here in **Markdown** format.
```

### Frontmatter Options

- `title` - Page title (required)
- `layout` - Layout to use (default: "wiki")
- `description` - Page description for SEO
- `date` - Publication date
- `author` - Author name
- `category` - Category for organization
- `toc` - Show table of contents (true/false)

### Markdown Features

- **Headers** - `# H1`, `## H2`, `### H3`
- **Bold/Italic** - `**bold**`, `*italic*`
- **Links** - `[text](url)`
- **Images** - `![alt](image.jpg)`
- **Code blocks** - ` ```language `
- **Tables** - Standard Markdown tables
- **Lists** - Ordered and unordered
- **Blockquotes** - `> quote`
- **And more!**

## Configuration

Edit `config.json` to customize your wiki:

```json
{
  "site_name": "My Wiki",
  "site_url": "https://username.github.io/wiki",
  "base_url": "",
  "site_description": "My documentation site",
  "author": "Your Name",
  "year": "2026",
  "show_search": true,
  "categories": [
    {
      "name": "Documentation",
      "slug": "documentation"
    }
  ]
}
```

## Building

### Build Command

```bash
./scripts/build.sh
```

### Clean Build

Remove output directory before building:

```bash
./scripts/build.sh --clean
```

### Using Python Directly

```bash
python scripts/markdown2html.py
python scripts/markdown2html.py --clean
```

## Deployment

### GitHub Pages (Recommended)

1. Create a new GitHub repository
2. Push your code:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/username/repo.git
git push -u origin main
```

3. Enable GitHub Pages in repository settings:
   - Go to Settings → Pages
   - Source: GitHub Actions

4. The workflow will automatically build and deploy on push!

### Manual Deployment

```bash
./scripts/deploy.sh
```

This will deploy the `output/` directory to the `gh-pages` branch.

### Other Platforms

The `output/` directory contains pure static HTML that can be deployed to:

- **Netlify** - Drag and drop the output folder
- **Vercel** - Connect your repository
- **AWS S3** - Upload to a public bucket
- **Cloudflare Pages** - Connect repository
- **Any web server** - Copy files to server root

## Customization

### Styling

The Tyrian theme is in `node_modules/@gentoo/tyrian/dist/`. To customize:

1. Copy `tyrian.min.css` to your project
2. Create custom CSS in `content/assets/custom.css`
3. Include it in `templates/base.html`

### Templates

Edit `templates/base.html` to modify the layout. The template uses Mustache syntax:

```html
{{title}}         <!-- Page title -->
{{content}}       <!-- Page content -->
{{site_name}}     <!-- Site name from config -->
{{base_url}}      <!-- Base URL from config -->
```

### Navigation

Edit the `sidebar_sections` in `config.json`:

```json
{
  "sidebar_sections": [
    {
      "title": "Quick Links",
      "links": [
        {
          "title": "Home",
          "url": "/index.html"
        }
      ]
    }
  ]
}
```

## Scripts

### build.sh

Builds the static site from markdown files.

```bash
./scripts/build.sh          # Build
./scripts/build.sh --clean  # Clean build
./scripts/build.sh --help   # Show help
```

### deploy.sh

Deploys to GitHub Pages (gh-pages branch).

```bash
./scripts/deploy.sh         # Deploy
./scripts/deploy.sh --help  # Show help
```

### markdown2html.py

Python build script. Can be used directly.

```bash
python scripts/markdown2html.py
python scripts/markdown2html.py --clean
python scripts/markdown2html.py --project-root /path/to/wiki
```

## Troubleshooting

### Theme Not Found

```bash
npm install git+https://anongit.gentoo.org/git/sites/tyrian-theme.git
```

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

- Verify theme is installed in `node_modules/@gentoo/tyrian/`
- Check that assets are being copied to `output/assets/`
- Clear browser cache and rebuild

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Credits

- **Tyrian Theme** by [Gentoo](https://www.gentoo.org/)
- Bootstrap 4.6.2
- Font Awesome 4.7.0
- Python Markdown library
- Mustache templating

## License

This project is licensed under the MIT License - see the LICENSE file for details.

The Tyrian theme is copyright by Gentoo Foundation.

## Support

- 📖 [Documentation](https://github.com/yourusername/static-wiki-tyrian/wiki)
- 🐛 [Issue Tracker](https://github.com/yourusername/static-wiki-tyrian/issues)
- 💬 [Discussions](https://github.com/yourusername/static-wiki-tyrian/discussions)

## Show Your Support

Give a ⭐️ if this project helped you!

---

**Built with ❤️ using [Tyrian Theme](https://www.gentoo.org/) from Gentoo**
