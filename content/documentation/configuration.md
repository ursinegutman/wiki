---
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
