# Static Wiki with Tyrian Theme - Project Summary

## Overview

A complete static wiki system that uses the beautiful Tyrian theme from Gentoo. Write content in Markdown, build to static HTML, and deploy anywhere.

## What's Included

### Core Features
✅ Markdown to HTML conversion
✅ Tyrian theme (Bootstrap 4 based)
✅ Responsive design (mobile-friendly)
✅ Table of contents generation
✅ Syntax highlighting for code blocks
✅ Category support
✅ Search integration
✅ GitHub Actions workflow for auto-deployment

### Project Structure
```
static-wiki-tyrian/
├── content/
│   └── wiki/              # Your markdown content
│       ├── index.md
│       ├── getting-started.md
│       ├── installation.md
│       └── configuration.md
├── templates/
│   └── base.html          # Main HTML template
├── scripts/
│   ├── build.sh           # Build script (wrapper)
│   ├── deploy.sh          # Deployment to GitHub Pages
│   └── markdown2html.py   # Core Python builder
├── output/                # Generated static HTML (auto-created)
├── .github/workflows/
│   ├── deploy.yml         # GitHub Pages deployment
│   └── ci.yml             # CI/testing workflow
├── config.json            # Site configuration
├── package.json           # npm dependencies
├── requirements.txt       # Python dependencies
├── README.md              # Full documentation
├── QUICKSTART.md          # Quick start guide
├── LICENSE                # MIT License
└── .gitignore             # Git ignore rules
```

## Installation

1. Clone the project
2. Install Python dependencies: `pip install -r requirements.txt`
3. Install Tyrian theme: `npm install`
4. Build: `./scripts/build.sh`

## Usage

### Writing Content

Create markdown files in `content/wiki/`:

```markdown
---
title: My Page
layout: wiki
description: Page description
toc: true
---

# Content here
```

### Building

```bash
./scripts/build.sh          # Build
./scripts/build.sh --clean  # Clean build
```

### Previewing

```bash
cd output
python3 -m http.server 8000
# Visit http://localhost:8000
```

### Deploying

**GitHub Pages (automatic):**
1. Push to GitHub
2. Enable Pages in settings
3. Select GitHub Actions as source
4. Done!

**Manual deployment:**
```bash
./scripts/deploy.sh
```

## Key Files

### Configuration
- `config.json` - All site settings
- `templates/base.html` - Main template

### Content
- `content/wiki/` - All markdown files

### Build System
- `scripts/markdown2html.py` - Core builder
- `scripts/build.sh` - Wrapper script
- `scripts/deploy.sh` - Deployment script

### Automation
- `.github/workflows/deploy.yml` - Auto-deploy to GitHub Pages
- `.github/workflows/ci.yml` - CI testing

## Frontmatter Options

```yaml
---
title: Page Title          # Required
layout: wiki              # Layout to use
description: SEO desc     # Page description
date: 2026-01-20         # Publication date
author: Author Name      # Page author
category: Category       # Content category
toc: true               # Show TOC (true/false)
---
```

## Dependencies

### Python (requirements.txt)
- markdown - Markdown parsing
- pystache - Mustache templating
- python-frontmatter - YAML frontmatter parsing
- Pygments - Code syntax highlighting

### Node.js (package.json)
- @gentoo/tyrian - The Tyrian theme (Bootstrap 4 based)

## Customization

### Site Configuration
Edit `config.json`:
- Site name, URL, description
- Navigation menu
- Sidebar sections
- Categories
- Search settings

### Styling
Edit `templates/base.html` or add custom CSS

### Templates
Modify `templates/base.html` to change layout

## Deployment Options

1. **GitHub Pages** - Recommended (automatic)
2. **Netlify** - Drag and drop
3. **Vercel** - Connect repository
4. **AWS S3** - Static hosting
5. **Any web server** - Copy output files

## Features

### Markdown Support
- Headers, paragraphs, lists
- Bold, italic, links
- Code blocks with syntax highlighting
- Tables
- Blockquotes
- And more!

### Theme Features
- Responsive navigation
- Sidebar with navigation
- Search integration
- Breadcrumbs
- Footer with copyright
- Mobile-friendly design

### Build Features
- Fast Python-based builder
- Clean builds (--clean flag)
- Asset copying
- TOC generation
- Error handling

## Scripts

### build.sh
```bash
./scripts/build.sh          # Build
./scripts/build.sh --clean  # Clean build
./scripts/build.sh --help   # Show help
```

### deploy.sh
```bash
./scripts/deploy.sh         # Deploy to gh-pages
./scripts/deploy.sh --help  # Show help
```

### markdown2html.py
```bash
python scripts/markdown2html.py
python scripts/markdown2html.py --clean
python scripts/markdown2html.py --project-root /path
```

## Sample Content Included

- Home page (index.md)
- Getting Started guide
- Installation guide
- Configuration guide

All samples show proper formatting and frontmatter.

## Documentation

- **README.md** - Full documentation
- **QUICKSTART.md** - 5-minute setup guide
- **content/wiki/** - Sample wiki content

## License

MIT License - see LICENSE file

The Tyrian theme is copyright by Gentoo Foundation.

## Credits

- **Tyrian Theme** by Gentoo Foundation
- **Bootstrap 4.6.2** - UI framework
- **Font Awesome 4.7.0** - Icons
- **Python Markdown** - Markdown processing
- **Mustache** - Templating engine

## Next Steps

1. Customize `config.json` with your site details
2. Create your content in `content/wiki/`
3. Build and preview locally
4. Deploy to GitHub Pages
5. Customize the theme to your liking

## Support

- GitHub Issues
- README documentation
- Sample content as reference

---

**Enjoy your new static wiki! 🎉**
