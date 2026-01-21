---
title: Getting Started
layout: wiki
description: Learn how to set up and use your static wiki with Tyrian theme
date: 2026-01-20
author: Wiki Admin
category: Guides
toc: true
---

# Getting Started with Static Wiki

This guide will help you get your static wiki up and running with the Tyrian theme.

## Prerequisites

Before you begin, make sure you have the following installed:

- **Node.js** (v14 or higher) - for installing the Tyrian theme
- **Python** (v3.7 or higher) - for the build scripts
- **Git** - for version control and deployment
- **Pip** - Python package manager

### Installing Dependencies

**Ubuntu/Debian:**

```bash
sudo apt update
sudo apt install nodejs npm python3 python3-pip git
```

**macOS:**

```bash
brew install node python3 git
```

**Windows:**

Download and install:
- [Node.js](https://nodejs.org/)
- [Python](https://www.python.org/downloads/)
- [Git for Windows](https://git-scm.com/download/win)

## Installation

### 1. Clone or Create Your Wiki

```bash
# If starting from this template
git clone https://github.com/yourusername/static-wiki-tyrian.git
cd static-wiki-tyrian

# Or create a new directory
mkdir my-wiki
cd my-wiki
```

### 2. Install Python Dependencies

```bash
pip install markdown pystache python-frontmatter
```

### 3. Install the Tyrian Theme

```bash
npm install git+https://anongit.gentoo.org/git/sites/tyrian-theme.git
```

## Project Structure

Understanding the directory layout:

```
static-wiki-tyrian/
├── content/
│   └── wiki/              # Your markdown content goes here
│       ├── index.md       # Home page
│       ├── page1.md       # Additional pages
│       └── category/      # Subdirectories for organization
│           └── page2.md
├── templates/             # HTML templates
│   └── base.html          # Main template with Tyrian theme
├── scripts/               # Build scripts
│   ├── build.sh          # Bash build script
│   └── markdown2html.py  # Python build script
├── output/               # Generated static HTML (auto-generated)
├── config.json           # Site configuration
└── README.md             # This file
```

## Creating Your First Page

### 1. Create a Markdown File

Create a new file in `content/wiki/`:

```bash
nano content/wiki/my-first-page.md
```

### 2. Add Frontmatter

Every page should start with YAML frontmatter:

```markdown
---
title: My First Page
layout: wiki
description: This is my first wiki page
date: 2026-01-20
author: Your Name
category: Guides
toc: true
---

# My First Page

This is the content of my first wiki page...
```

### 3. Write Your Content

Use standard Markdown syntax:

```markdown
## Heading 2

This is a paragraph with **bold** and *italic* text.

### Lists

- Item 1
- Item 2
- Item 3

### Code Blocks

```python
def hello():
    print("Hello, World!")
```

### Links

[Link to another page](other-page.html)
```

## Building Your Wiki

### Using the Python Script (Recommended)

```bash
python3 scripts/markdown2html.py
```

### Using the Bash Script

```bash
chmod +x scripts/build.sh
./scripts/build.sh
```

### Build Options

Clean build (remove output directory first):

```bash
python3 scripts/markdown2html.py --clean
```

Specify project root:

```bash
python3 scripts/markdown2html.py --project-root /path/to/wiki
```

## Previewing Your Wiki

### Simple HTTP Server

```bash
cd output
python3 -m http.server 8000
```

Then visit: http://localhost:8000

### Using Live Server (VS Code)

1. Install the "Live Server" extension
2. Right-click on `output/index.html`
3. Select "Open with Live Server"

## Configuration

Edit `config.json` to customize your wiki:

```json
{
  "site_name": "My Awesome Wiki",
  "site_url": "https://username.github.io/my-wiki",
  "base_url": "",
  "site_description": "Documentation for my project",
  "author": "Your Name",
  "show_search": true,
  "categories": [
    {
      "name": "Documentation",
      "slug": "documentation"
    }
  ]
}
```

## Organizing Content

### Directory Structure

Organize your content with directories:

```
content/wiki/
├── index.md
├── guides/
│   ├── index.md
│   ├── getting-started.md
│   └── advanced-topics.md
├── reference/
│   ├── index.md
│   ├── api.md
│   └── cli.md
└── tutorials/
    └── example.md
```

### Categories and Tags

Add categories to frontmatter:

```markdown
---
title: Advanced Configuration
category: Documentation
tags: [config, advanced]
---
```

## Next Steps

Now that you have your wiki set up:

1. **Create more content** - Add your documentation pages
2. **Customize the theme** - Modify templates in `templates/`
3. **Configure navigation** - Update `config.json`
4. **Build your site** - Run the build script
5. **Deploy** - Follow the [Deployment Guide](deployment.html)

## Troubleshooting

### Theme Assets Not Found

If you see missing styles:

```bash
# Reinstall the Tyrian theme
npm install git+https://anongit.gentoo.org/git/sites/tyrian-theme.git
```

### Python Dependencies Missing

```bash
pip install --upgrade markdown pystache python-frontmatter
```

### Build Errors

1. Check that all markdown files have valid frontmatter
2. Verify the `content/wiki/` directory exists
3. Ensure `config.json` is valid JSON

## Getting Help

- Check the [FAQ](faq.html)
- Review [sample content](sample-content.html)
- Open an issue on GitHub

---

**Ready to deploy? See the [Deployment Guide](deployment.html).**
