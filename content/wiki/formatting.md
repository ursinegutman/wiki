---
title: Formatting Guide
layout: wiki
description: Examples of Gentoo Wiki formatting
toc: true
---

# Formatting Guide

This page demonstrates the various formatting options available in the wiki.

## Command Boxes

You can use command boxes to show terminal commands:

Root commands:
```cmd root
emerge --ask app-editors/vim
systemctl restart nginx
```

User commands:
```cmd user
git clone https://github.com/ursinegutman/wiki.git
cd wiki
```

## Code Boxes with File Captions

Show configuration files with path and description:

```file /etc/conf.d/hostname
# Set the hostname of the system
hostname="mygentoo"
```

```file ~/.bashrc Sample bash configuration
export EDITOR=vim
alias ll='ls -lh'
```

## Alert Boxes

### Warning Alerts
```warning
Important
Always backup your data before making system changes!
```

### Success Alerts
```success
Tip
The Gentoo Handbook is an excellent resource for learning about the system.
```

### Info Alerts
```info
Note
This wiki uses Markdown for content formatting.
```

### Danger Alerts
```danger
Warning
Running commands as root can be dangerous - double check before executing!
```

## Tables

| Input | Rendered output | Use case | Example within text |
|-------|----------------|----------|---------------------|
| `''italics''` | *italics* | To emphasize something | It is *not possible* to change the order |
| `'''bold'''` | **bold** | To strongly emphasize something | Using the hyphen is **absolutely** necessary |
| `<code>foo</code>` | `foo` | Small chunks of code inline | Set the value to `-alsa` to disable support |

## Standard Code Blocks

Regular code blocks still work:

```python
def hello():
    print("Hello, Gentoo!")
```

```bash
#!/bin/bash
echo "This is a bash script"
```
