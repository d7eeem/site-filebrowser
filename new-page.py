#!/usr/bin/env python3

import sys
import os
from datetime import datetime
from pathlib import Path

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="/style.css">
</head>
<body>
<main>
<h1>{title}</h1>
<p>-</p>

<p>Start writing your content here...</p>

<time>{date}</time>

</main>
<footer>
<p><a href="../"><i>../</i></a></p>
<button class="theme-toggle" onclick="toggleTheme()">◐</button>
</footer>
<script>
function toggleTheme() {{
  document.body.classList.toggle('dark');
}}
</script>
</body>
</html>"""

def create_page(title, filepath):
    """Create a new HTML page from template"""
    
    # Ensure .html extension
    if not filepath.endswith('.html'):
        filepath += '.html'
    
    # Full path
    full_path = Path('html') / filepath
    
    # Create parent directories
    full_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Get current date
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Generate HTML content
    html_content = TEMPLATE.format(
        title=title,
        date=current_date
    )
    
    # Write file
    with open(full_path, 'w') as f:
        f.write(html_content)
    
    print(f"✓ Created: {full_path}")
    print(f"  Title: {title}")
    print(f"  Date: {current_date}")
    print(f"\nEdit with: nano {full_path}")
    
    return full_path

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 new-page.py \"Page Title\" path/to/file.html")
        print("\nExamples:")
        print("  python3 new-page.py \"My Blog Post\" posts/my-post.html")
        print("  python3 new-page.py \"About Me\" about.html")
        print("  python3 new-page.py \"Deep Page\" projects/web/deep/page.html")
        sys.exit(1)
    
    title = sys.argv[1]
    filepath = sys.argv[2]
    
    create_page(title, filepath)

if __name__ == '__main__':
    main()
