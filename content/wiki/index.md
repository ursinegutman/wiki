---
title: Welcome to Static Wiki
layout: wiki
description: A static wiki powered by Tyrian theme from Gentoo
date: 2026-01-20
author: Wiki Admin
category: Documentation
toc: true
---

# Welcome to Static Wiki

Welcome to your new **static wiki** powered by the beautiful **Tyrian theme** from Gentoo!

This wiki system allows you to create documentation, knowledge bases, or personal wikis using simple Markdown files, which are then converted to static HTML that can be hosted anywhere - including GitHub Pages.

## Features

- 🎨 **Beautiful Tyrian Theme** - The same theme used by Gentoo Wiki
- 📝 **Markdown Authoring** - Write content in familiar Markdown format
- 🚀 **Static Site Generation** - Fast, secure, and easy to deploy
- 📱 **Responsive Design** - Works perfectly on mobile, tablet, and desktop
- 🔍 **Search Integration** - Built-in Google Custom Search support
- 📂 **Category Support** - Organize content into categories
- 🔄 **Git-Based Workflow** - Version control for your documentation
- 🌐 **GitHub Pages Ready** - Deploy with a simple git push

## Quick Start

### 1. Create Content

Write your wiki pages in Markdown in the `content/wiki/` directory:

```bash
content/wiki/
├── index.md
├── getting-started.md
├── installation.md
└── configuration.md
```

### 2. Build the Site

Run the build script to generate static HTML:

```bash
./scripts/build.sh
```

Or use the Python builder:

```bash
python3 scripts/markdown2html.py
```

### 3. Deploy

The generated HTML files in `output/` can be deployed to any static hosting service:

- **GitHub Pages** - Push to gh-pages branch
- **Netlify** - Drag and drop the output folder
- **Vercel** - Connect your repository
- **AWS S3** - Upload to a public bucket
- **Any web server** - Copy the files

## Sample Content

Explore these sample pages to learn more:

- [Getting Started Guide](getting-started.html)
- [Installation Instructions](installation.html)
- [Configuration Options](configuration.html)
- [Content Creation Guide](content-creation.html)
- [Deployment Guide](deployment.html)

## Code Examples

You can include syntax-highlighted code blocks:

```python
def greet(name):
    """Greet someone by name"""
    return f"Hello, {name}!"

print(greet("World"))
```

```bash
# Build your static wiki
cd static-wiki-tyrian
./scripts/build.sh

# Deploy to GitHub Pages
git add .
git commit -m "Update wiki"
git push
```

```javascript
// Example JavaScript code
function calculateSum(a, b) {
    return a + b;
}

console.log(calculateSum(5, 3)); // Output: 8
```

## Tables

You can create formatted tables:

| Feature | Status | Notes |
|---------|--------|-------|
| Markdown support | ✅ Complete | Full CommonMark + GitHub Flavored Markdown |
| Tyrian theme | ✅ Complete | Bootstrap 4 based theme |
| Responsive design | ✅ Complete | Mobile-first approach |
| Search | ✅ Complete | Google Custom Search integration |
| Syntax highlighting | ✅ Complete | Pygments support |
| Table of contents | ✅ Complete | Auto-generated from headings |

## Alerts and Callouts

!!! note
    This is a note alert. Use it for additional information or context.

!!! warning
    This is a warning alert. Use it for important warnings or cautions.

!!! tip
    This is a tip alert. Use it for helpful tips and best practices.

## Next Steps

1. **Read the [Getting Started Guide](getting-started.html)** to learn the basics
2. **Customize the [Configuration](configuration.html)** for your needs
3. **Create your first page** in the `content/wiki/` directory
4. **Build and deploy** your wiki to share with the world

## Contributing

Found a bug or have a suggestion? Please open an issue or submit a pull request on GitHub!

---

**Happy documenting! 📚**
