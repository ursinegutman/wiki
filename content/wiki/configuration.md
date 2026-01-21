---
title: Configuration Guide
layout: wiki
description: Learn how to configure your static wiki
date: 2026-01-20
author: Wiki Admin
category: Documentation
toc: true
---

# Configuration Guide

This guide covers all the configuration options for your static wiki.

## Main Configuration File

The `config.json` file in the root directory contains all your site settings:

```json
{
  "site_name": "My Wiki",
  "site_url": "https://username.github.io/wiki",
  "base_url": "",
  "site_description": "My documentation site",
  "language": "en",
  "author": "Wiki Admin",
  "year": "2026",
  "show_search": true,
  "categories": [...],
  "sidebar_sections": [...]
}
```

## Configuration Options

### Site Information

#### site_name
The name of your wiki. Appears in the header, page titles, and footer.

```json
"site_name": "My Awesome Wiki"
```

#### site_url
The full URL where your wiki will be hosted. Used for RSS feeds and SEO.

```json
"site_url": "https://username.github.io/my-wiki"
```

For GitHub Pages:
- User/organization site: `https://username.github.io`
- Project site: `https://username.github.io/repository-name`

#### base_url
Base path for your site if hosted in a subdirectory.

```json
"base_url": ""
```

Leave empty for root hosting. Use subdirectory path if needed:
```json
"base_url": "/wiki"
```

#### site_description
Description of your wiki for SEO and metadata.

```json
"site_description": "Documentation for my awesome project"
```

#### language
Site language code.

```json
"language": "en"
```

### Author Information

#### author
Default author name for pages without author specified.

```json
"author": "Your Name"
```

#### year
Copyright year shown in footer.

```json
"year": "2026"
```

### Features

#### show_search
Enable/disable the search box in sidebar.

```json
"show_search": true
```

When enabled, uses Google Custom Search restricted to your domain.

### Navigation

#### categories
List of categories for the dropdown menu.

```json
"categories": [
  {
    "name": "Documentation",
    "slug": "documentation"
  },
  {
    "name": "Guides",
    "slug": "guides"
  },
  {
    "name": "API Reference",
    "slug": "api"
  }
]
```

#### sidebar_sections
Navigation sections and links for the sidebar.

```json
"sidebar_sections": [
  {
    "title": "Getting Started",
    "links": [
      {
        "title": "Installation",
        "url": "/wiki/installation.html"
      },
      {
        "title": "Quick Start",
        "url": "/wiki/quickstart.html"
      }
    ]
  }
]
```

## Page Configuration

Each markdown file can have its own configuration via frontmatter:

```markdown
---
title: Page Title
layout: wiki
description: Page description
date: 2026-01-20
author: Author Name
category: Documentation
toc: true
---
```

### Page Frontmatter Options

#### title (required)
Page title. Appears in `<h1>` and `<title>` tag.

#### layout
Template layout to use. Default: `wiki`

Available layouts:
- `wiki` - Standard wiki page with sidebar
- `home` - Homepage layout
- `minimal` - Minimal layout without sidebar

#### description
Page description for SEO and metadata.

#### date
Publication date. Format: `YYYY-MM-DD`

#### author
Page author name. Overrides site default.

#### category
Category for organizing content.

#### toc
Enable/disable table of contents. Values: `true` or `false`

#### template
Custom template file to use. Default: `base.html`

## Environment-Specific Configuration

### Development

For local development:

```json
{
  "site_url": "http://localhost:8000",
  "base_url": ""
}
```

### Production

For GitHub Pages:

```json
{
  "site_url": "https://username.github.io/repo-name",
  "base_url": "/repo-name"
}
```

Or for custom domain:

```json
{
  "site_url": "https://wiki.example.com",
  "base_url": ""
}
```

## Advanced Configuration

### Custom CSS

Add custom styles by creating `content/assets/custom.css`:

```css
/* Custom styles */
.wiki-content {
  font-size: 1.1em;
}

.custom-highlight {
  background-color: #ffffcc;
  padding: 1rem;
  border-left: 4px solid #ffcc00;
}
```

### Custom JavaScript

Add custom scripts by editing `templates/base.html`:

```html
<script>
// Custom JavaScript
document.addEventListener('DOMContentLoaded', function() {
    console.log('Wiki loaded!');
});
</script>
```

### Modifying Templates

The `templates/base.html` file controls the page layout. Key sections:

- `<header>` - Site header and navigation
- `<aside>` - Sidebar content
- `<main>` - Main content area
- `<footer>` - Site footer

### Search Configuration

To use custom search:

1. Create a Google Custom Search engine at https://programmablesearch.google.com/
2. Configure it to search only your site
3. Get your Search Engine ID (CX)
4. Modify the search form in `templates/base.html`:

```html
<form action="https://cse.google.com/cse" method="get">
  <input type="hidden" name="cx" value="YOUR_SEARCH_ENGINE_ID">
  <input type="text" name="q" class="form-control">
  <button type="submit">Search</button>
</form>
```

### Analytics

Add analytics by modifying `templates/base.html`:

**Google Analytics:**

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_TRACKING_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_TRACKING_ID');
</script>
```

**Plausible Analytics:**

```html
<!-- Plausible Analytics -->
<script defer data-domain="yourdomain.com" src="https://plausible.io/js/plausible.js"></script>
```

## Example Configurations

### Personal Wiki

```json
{
  "site_name": "John's Knowledge Base",
  "site_url": "https://john.github.io/wiki",
  "site_description": "Personal knowledge base and notes",
  "author": "John Doe",
  "show_search": true,
  "categories": [
    {"name": "Notes", "slug": "notes"},
    {"name": "Projects", "slug": "projects"}
  ]
}
```

### Project Documentation

```json
{
  "site_name": "Project XYZ Documentation",
  "site_url": "https://docs.example.com",
  "site_description": "Official documentation for Project XYZ",
  "author": "XYZ Team",
  "show_search": true,
  "categories": [
    {"name": "Getting Started", "slug": "getting-started"},
    {"name": "API Reference", "slug": "api"},
    {"name": "Tutorials", "slug": "tutorials"}
  ]
}
```

### Team Knowledge Base

```json
{
  "site_name": "Company Wiki",
  "site_url": "https://wiki.company.com",
  "site_description": "Internal company documentation",
  "author": "Documentation Team",
  "show_search": true,
  "categories": [
    {"name": "Policies", "slug": "policies"},
    {"name": "Procedures", "slug": "procedures"},
    {"name": "Projects", "slug": "projects"}
  ]
}
```

## Troubleshooting Configuration

### Site Not Loading CSS

Check `base_url` in config.json. If your site is in a subdirectory, set it:

```json
"base_url": "/wiki"
```

### Search Not Working

Verify:
1. `show_search` is `true` in config
2. `site_domain` is correctly set
3. Google has indexed your site (takes time after deployment)

### Navigation Links Broken

Ensure URLs in `sidebar_sections` start with `/`:

```json
{
  "url": "/wiki/page.html"  // Correct
}
```

Not:

```json
{
  "url": "wiki/page.html"  // Wrong - missing leading slash
}
```

## Next Steps

- [Content Creation Guide](content-creation.html)
- [Deployment Guide](deployment.html)
- [Customization Guide](customization.html)

---

**Need help? Check the [FAQ](faq.html) or open an issue.**
