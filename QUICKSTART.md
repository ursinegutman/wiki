# Quick Start Guide

Get your static wiki up and running in 5 minutes!

## Step 1: Install Dependencies

```bash
# Install Python packages
pip install markdown pystache python-frontmatter

# Install Tyrian theme
npm install git+https://anongit.gentoo.org/git/sites/tyrian-theme.git
```

## Step 2: Create Your First Page

Edit `content/wiki/index.md`:

```markdown
---
title: Welcome to My Wiki
layout: wiki
description: My awesome wiki
toc: true
---

# Welcome to My Wiki

This is my first page!
```

## Step 3: Build

```bash
./scripts/build.sh
```

## Step 4: Preview

```bash
cd output
python3 -m http.server 8000
```

Visit http://localhost:8000

## Step 5: Deploy to GitHub Pages

```bash
# Initialize git
git init
git add .
git commit -m "Initial commit"

# Add remote (replace with your repo)
git remote add origin https://github.com/username/repo.git
git branch -M main
git push -u origin main

# Enable GitHub Pages in repo settings
# Settings → Pages → Source: GitHub Actions
```

That's it! Your wiki will be live at `https://username.github.io/repo`

## Next Steps

- Read the [Getting Started Guide](content/wiki/getting-started.md)
- Configure your wiki in `config.json`
- Add more content in `content/wiki/`
- Customize the theme

## Need Help?

- Check the [FAQ](content/wiki/faq.md)
- Review [Configuration Guide](content/wiki/configuration.md)
- Open an issue on GitHub
