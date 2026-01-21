---
title: Installation Guide
layout: wiki
description: Detailed installation instructions for the static wiki with Tyrian theme
date: 2026-01-20
author: Wiki Admin
category: Documentation
toc: true
---

# Installation Guide

This guide provides detailed installation instructions for setting up your static wiki with the Tyrian theme.

## System Requirements

### Minimum Requirements

- **Node.js**: v14.0.0 or higher
- **Python**: v3.7 or higher
- **Git**: v2.0 or higher
- **Disk Space**: ~100 MB for dependencies

### Recommended

- **Node.js**: v18 LTS or higher
- **Python**: v3.10 or higher
- **RAM**: 2GB or more
- **Disk Space**: 500MB or more

## Installation Methods

### Method 1: Clone from Template (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/static-wiki-tyrian.git
cd static-wiki-tyrian

# Install Python dependencies
pip install -r requirements.txt

# Install the Tyrian theme
npm install
```

### Method 2: Manual Setup

```bash
# Create project directory
mkdir my-wiki
cd my-wiki

# Create directory structure
mkdir -p content/wiki templates scripts output

# Download build scripts
# (Copy scripts from the template repository)

# Create config.json
# (Copy config from the template repository)

# Install dependencies
pip install markdown pystache python-frontmatter
npm install git+https://anongit.gentoo.org/git/sites/tyrian-theme.git
```

### Method 3: Docker Setup

Create a `Dockerfile`:

```dockerfile
FROM python:3.10-slim

# Install Node.js
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
RUN apt-get install -y nodejs git

# Set working directory
WORKDIR /wiki

# Copy project files
COPY . .

# Install dependencies
RUN pip install markdown pystache python-frontmatter
RUN npm install git+https://anongit.gentoo.org/git/sites/tyrian-theme.git

# Run build
CMD ["python3", "scripts/markdown2html.py"]
```

Build and run:

```bash
docker build -t static-wiki .
docker run -v $(pwd)/output:/wiki/output static-wiki
```

## Detailed Dependency Installation

### Node.js and npm

**Ubuntu/Debian:**

```bash
# Using NodeSource repository (recommended)
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Or using apt
sudo apt update
sudo apt install nodejs npm
```

**macOS:**

```bash
# Using Homebrew
brew install node

# Verify installation
node --version
npm --version
```

**Windows:**

Download the installer from [nodejs.org](https://nodejs.org/)

### Python and pip

**Ubuntu/Debian:**

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

**macOS:**

Python usually comes pre-installed. To upgrade:

```bash
brew install python@3.10
```

**Windows:**

Download from [python.org](https://www.python.org/downloads/)

### Git

**Ubuntu/Debian:**

```bash
sudo apt install git
```

**macOS:**

```bash
brew install git
```

**Windows:**

Download from [git-scm.com](https://git-scm.com/download/win)

## Python Package Installation

Create a `requirements.txt` file:

```txt
markdown>=3.4.1
pystache>=0.5.4
python-frontmatter>=1.0.0
Pygments>=2.14.0
```

Install dependencies:

```bash
# System-wide installation
pip install -r requirements.txt

# Or using virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Installing the Tyrian Theme

### From Gentoo Git Repository

```bash
npm install git+https://anongit.gentoo.org/git/sites/tyrian-theme.git
```

### Verify Installation

Check that the theme is installed:

```bash
ls node_modules/@gentoo/tyrian/dist/
```

You should see:
- `tyrian.min.css`
- `bootstrap.min.js`
- `jquery-3.6.slim.js`
- And other asset files

## Post-Installation Setup

### 1. Configure Your Wiki

Edit `config.json`:

```json
{
  "site_name": "My Wiki",
  "site_url": "https://username.github.io/my-wiki",
  "base_url": "",
  "site_description": "My documentation site",
  "author": "Your Name",
  "year": "2026",
  "show_search": true
}
```

### 2. Create Your First Page

Create `content/wiki/index.md`:

```markdown
---
title: Welcome
layout: wiki
description: Welcome to my wiki
---

# Welcome to My Wiki

This is my first wiki page!
```

### 3. Build the Site

```bash
python3 scripts/markdown2html.py
```

### 4. Test Locally

```bash
cd output
python3 -m http.server 8000
```

Visit: http://localhost:8000

## Verification Steps

### Check Dependencies

```bash
# Check Node.js version
node --version  # Should be v14+

# Check Python version
python3 --version  # Should be 3.7+

# Check npm packages
npm list  # Should show @gentoo/tyrian

# Check Python packages
pip list  # Should show markdown, pystache, etc.
```

### Test Build

```bash
# Run the build script
python3 scripts/markdown2html.py

# Check output directory
ls output/
```

Expected output:
```
assets/
index.html
wiki/
└── index.html
```

### Test Theme Assets

Verify that theme assets are copied:

```bash
ls output/assets/
```

Should include:
- `tyrian.min.css`
- `bootstrap.min.js`
- `site-logo.svg`
- Fonts and images

## Troubleshooting

### Issue: npm install fails

**Solution:**

```bash
# Clear npm cache
npm cache clean --force

# Try with legacy provider
npm install --legacy-peer-deps git+https://anongit.gentoo.org/git/sites/tyrian-theme.git
```

### Issue: Python module not found

**Solution:**

```bash
# Ensure you're using the correct Python
python3 -m pip install markdown pystache python-frontmatter

# Or use virtual environment
python3 -m venv venv
source venv/bin/activate
pip install markdown pystache python-frontmatter
```

### Issue: Theme assets not loading

**Solution:**

```bash
# Reinstall theme
npm uninstall git+https://anongit.gentoo.org/git/sites/tyrian-theme.git
npm install git+https://anongit.gentoo.org/git/sites/tyrian-theme.git

# Rebuild
python3 scripts/markdown2html.py --clean
```

### Issue: Permission errors

**Solution:**

```bash
# Use virtual environment instead of system-wide install
python3 -m venv venv
source venv/bin/activate
pip install --user markdown pystache python-frontmatter
```

## Uninstallation

To remove the wiki and its dependencies:

```bash
# Remove the wiki directory
rm -rf static-wiki-tyrian

# Remove global Python packages (if installed globally)
pip uninstall markdown pystache python-frontmatter Pygments

# Remove npm packages from the project
npm uninstall @gentoo/tyrian
```

## Upgrading

### Upgrade Python Dependencies

```bash
pip install --upgrade markdown pystache python-frontmatter Pygments
```

### Upgrade Tyrian Theme

```bash
npm update git+https://anongit.gentoo.org/git/sites/tyrian-theme.git
```

### Update Build Scripts

```bash
git pull origin main
```

## Next Steps

After installation:

1. ✅ Read the [Getting Started Guide](getting-started.html)
2. ✅ Configure your wiki in `config.json`
3. ✅ Create your content in `content/wiki/`
4. ✅ Build and test locally
5. ✅ Deploy to production (see [Deployment Guide](deployment.html))

---

**Installation complete! Ready to start creating your wiki. 🎉**
