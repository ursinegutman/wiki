---
title: Content Examples
layout: wiki
description: Examples of all Markdown features and formatting
date: 2026-01-20
author: Wiki Admin
category: Documentation
toc: true
---

# Content Examples

This page demonstrates all the Markdown features and formatting options available in your static wiki.

## Text Formatting

You can write **bold text**, *italic text*, or ***both***. You can also use ~~strikethrough~~ for deleted text.

## Headings

Headings are created with `#` symbols:

```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
```

## Lists

### Unordered Lists

- Item 1
- Item 2
  - Nested item
  - Another nested item
- Item 3

### Ordered Lists

1. First item
2. Second item
   1. Nested item
   2. Another nested item
3. Third item

### Task Lists

- [x] Completed task
- [ ] Incomplete task
- [ ] Another task

## Links

### External Links

[Visit GitHub](https://github.com)

### Internal Links

[Home Page](index.html)
[Getting Started](getting-started.html)

### Link with Title

[GitHub](https://github.com "GitHub Homepage")

## Images

### Local Images

```
![Alt text](path/to/image.jpg)
```

### External Images

### Images with Titles

```
![Alt text](image.jpg "Image title")
```

## Code

### Inline Code

Use `backticks` for `inline code`.

### Code Blocks

#### Python

```python
def fibonacci(n):
    """Generate Fibonacci sequence"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Print first 10 Fibonacci numbers
for num in fibonacci(10):
    print(num)
```

#### Bash/Shell

```bash
#!/bin/bash

# Build the wiki
echo "Building wiki..."
./scripts/build.sh

# Deploy to GitHub Pages
echo "Deploying..."
./scripts/deploy.sh
```

#### JavaScript

```javascript
// Example JavaScript
function calculateSum(a, b) {
    return a + b;
}

const result = calculateSum(5, 3);
console.log(`Result: ${result}`);
```

#### CSS

```css
/* Custom CSS example */
.wiki-content {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
}

.highlight {
    background-color: #ffffcc;
    padding: 1rem;
    border-radius: 4px;
}
```

### Inline Code with Language

You can also specify the language for syntax highlighting:

``````markdown
```python
def hello():
    print("Hello, World!")
```
``````

## Tables

### Basic Table

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |

### Aligned Table

| Left | Center | Right |
|:-----|:------:|------:|
| Left | Center | Right |
| L    | C      | R      |

### Table with Formatting

| Feature | Status | Notes |
|---------|--------|-------|
| **Markdown** | ✅ | Full support |
| *Tables* | ✅ | Aligned tables |
| `Code` | ✅ | Syntax highlighting |
| [Links](#) | ✅ | Internal and external |

## Blockquotes

### Simple Blockquote

> This is a simple blockquote.

### Blockquote with Multiple Paragraphs

> This is the first paragraph of the blockquote.
>
> This is the second paragraph.

### Nested Blockquotes

> This is the first level
>
> > This is a nested blockquote
> >
> > > You can nest further

### Blockquote with Other Elements

> #### Quoted Heading
>
> You can include other Markdown elements:
>
> - Lists
> - **Bold text**
> - `Code`
>
> All within a blockquote.

## Horizontal Rules

Horizontal rules are created with three or more dashes, asterisks, or underscores:

---

***

___

## Escaping Characters

To display literal Markdown characters, escape them with backslashes:

\*Not italic\*
\[Not a link\](#)
\`Not code\`

## HTML

You can use raw HTML in your Markdown:

### HTML Tags

<div style="background: #f0f0f0; padding: 1rem; border-radius: 4px;">
    This is a div with custom styling.
</div>

### HTML Attributes

You can add attributes to Markdown elements:

<img src="image.jpg" alt="Description" width="300" />

## Emojis

You can include emojis directly:

- :smile:
- :heart:
- :thumbsup:
- :book:
- :rocket:

## Math (if configured)

### Inline Math

The Pythagorean theorem is $a^2 + b^2 = c^2$.

### Block Math

$$
E = mc^2
$$

## Footnotes

Here's a sentence with a footnote [^1].

[^1]: This is the footnote content.

## Admonitions/Callouts

!!! note
    This is a note callout.

!!! warning
    This is a warning callout.

!!! tip
    This is a tip callout.

!!! important
    This is important information.

## Definition Lists

Term 1
:   Definition 1

Term 2
:   Definition 2a
:   Definition 2b

## Abbreviations

HTML is the standard markup language for documents.

The CSS is designed to enable the separation of document content.

## Combining Elements

You can combine multiple elements:

### Code in Lists

1. **Python**
   ```python
   print("Hello")
   ```

2. **JavaScript**
   ```javascript
   console.log("Hello");
   ```

### Blockquotes with Lists

> Important reminders:
>
> - First item
> - Second item
> - Third item

## Best Practices

1. **Use consistent heading levels** - Don't skip levels (H1 to H3)
2. **Add blank lines** - Between block elements for proper parsing
3. **Escape special characters** - When you want them displayed literally
4. **Use code blocks** - For code with proper syntax highlighting
5. **Add alt text** - For images to improve accessibility
6. **Use descriptive links** - Instead of "click here"
7. **Test your markdown** - Build and preview before deploying

## Tips

- Keep lines under 80-100 characters for readability
- Use `<!-- HTML comments -->` for notes that won't appear in output
- Use frontmatter for metadata
- Enable TOC for long documents
- Use categories for organization
- Add descriptions for SEO

## Common Issues

### Tables Not Rendering

Make sure there are blank lines before and after tables:

```markdown
Some text above

| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |

Some text below
```

### Code Blocks Not Highlighting

Specify the language after the opening triple backticks:

````markdown
```python
def hello():
    pass
```
````

### Links Not Working

- Use relative paths for internal links: `page.html`
- Use absolute URLs for external: `https://example.com`
- Ensure target files exist

## Resources

- [CommonMark Spec](https://spec.commonmark.org/)
- [GitHub Flavored Markdown](https://github.github.com/gfm/)
- [Markdown Guide](https://www.markdownguide.org/)

---

**Ready to create your own content? Start writing in `content/wiki/`!**
