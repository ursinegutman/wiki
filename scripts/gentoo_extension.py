#!/usr/bin/env python3
"""
Custom Markdown extension for Gentoo Wiki formatting
Supports:
- Cmd boxes (root/user commands)
- Code boxes with file captions
- Alert boxes (warning, success, info, danger)
"""

import re
from markdown import Extension
from markdown.preprocessors import Preprocessor
from xml.etree import ElementTree as etree


class GentooPreprocessor(Preprocessor):
    """Preprocessor to convert Gentoo syntax to HTML before markdown processing"""

    # Pattern for command boxes: ```cmd root or ```cmd user
    CMD_PATTERN = re.compile(r'```cmd\s+(root|user)\s*\n(.*?)```', re.DOTALL)

    # Pattern for file boxes: ```file /path/to/file description
    FILE_PATTERN = re.compile(r'```file\s+([^\n]+?)(?:\s+(.+?))?\n(.*?)```', re.DOTALL)

    # Pattern for alert boxes: ```warning, ```success, ```info, ```danger
    ALERT_PATTERN = re.compile(r'```(warning|success|info|danger)\s*\n(.*?)\n(.*?)```', re.DOTALL)

    ALERT_ICONS = {
        'warning': ('fa-exclamation-circle', 'Important'),
        'success': ('fa-check-circle', 'Tip'),
        'info': ('fa-sticky-note-o fa-rotate-180', 'Note'),
        'danger': ('fa-exclamation-triangle', 'Warning')
    }

    def run(self, lines):
        """Process the text and convert Gentoo syntax to HTML"""

        # Join lines for processing
        text = '\n'.join(lines)

        # Process command boxes
        text = self.CMD_PATTERN.sub(self._replace_cmd, text)

        # Process file boxes
        text = self.FILE_PATTERN.sub(self._replace_file, text)

        # Process alert boxes
        text = self.ALERT_PATTERN.sub(self._replace_alert, text)

        # Split back to lines
        return text.split('\n')

    def _replace_cmd(self, match):
        """Replace command box with HTML"""
        cmd_type = match.group(1)
        command = match.group(2).strip()

        if cmd_type == 'root':
            prompt_style = 'color: #ef2929; user-select: none; font-weight: bold;'
            prompt_span = '<span style="color: royalblue;">#</span>'
            prompt_text = 'root '
        else:  # user
            prompt_style = 'color: #4E9A06; user-select: none; font-weight: bold;'
            prompt_span = '<span style="color: royalblue;">$</span>'
            prompt_text = 'user '

        return f'''<div class="cmd-box"><div><code style="{prompt_style}">{prompt_text}{prompt_span}</code><code>{self._escape_html(command)}</code></div></div>'''

    def _replace_file(self, match):
        """Replace file box with HTML"""
        file_path = match.group(1).strip()
        description = match.group(2).strip() if match.group(2) else ''
        content = match.group(3).strip()

        caption_parts = [
            '<div class="box-caption">',
            '<span class="label" style="margin-right: .5em; background-color: #54487A">FILE</span>',
            f'<code style="border: none; background: none; color: #54487A; margin-right: .5em;">{self._escape_html(file_path)}</code>'
        ]

        if description:
            caption_parts.append(f'<strong>{self._escape_html(description)}</strong>')

        caption_parts.append('</div>')

        return f'''{''.join(caption_parts)}
<pre><code>{self._escape_html(content)}</code></pre>'''

    def _replace_alert(self, match):
        """Replace alert box with HTML"""
        alert_type = match.group(1)
        title_line = match.group(2).strip()
        content = match.group(3).strip()

        icon_class, default_title = self.ALERT_ICONS[alert_type]

        # If title line is empty or just whitespace, use default
        title = title_line if title_line else default_title

        return f'''<div class="alert alert-{alert_type} gw-box" style="padding-top: 8px; padding-bottom: 8px;">
<strong><i class="fa {icon_class}"></i> {self._escape_html(title)}</strong><br>
{self._escape_html(content)}
</div>'''

    def _escape_html(self, text):
        """Escape HTML special characters"""
        return (text
                .replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace("'", '&#39;'))


class GentooExtension(Extension):
    """Gentoo Wiki markdown extension"""

    def extendMarkdown(self, md):
        # Register preprocessor with very high priority to run BEFORE fenced code blocks
        # Fenced code blocks run at priority 180, so we need 200 or higher
        md.preprocessors.register(GentooPreprocessor(md), 'gentoo_preprocessor', 1000)


def makeExtension(**kwargs):
    """Return an instance of the extension"""
    return GentooExtension(**kwargs)
