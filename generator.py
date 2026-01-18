#!/usr/bin/env python3
import os
import time
from datetime import datetime
from pathlib import Path

# Exclusion patterns
EXCLUDE_PATTERNS = {
    '.git', 'node_modules', '.DS_Store', '__pycache__', '.env',
    'index.html',
    'style.css', 'template.html',
    'new-page.sh', 'new-page.py',
    '.gitignore', 'README.md'
}

def format_size(size):
    """Format file size in bytes to human readable format"""
    if size < 1024:
        return f"{size}B"
    elif size < 1024 * 1024:
        return f"{size // 1024}K"
    else:
        return f"{size // (1024 * 1024)}M"

def get_file_info(path):
    """Get file size and modification time"""
    stat = path.stat()
    size = stat.st_size
    mtime = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d')
    return format_size(size), mtime

def should_exclude(name):
    """Check if file/folder should be excluded"""
    return name in EXCLUDE_PATTERNS or name.startswith('.')

def generate_html(directory):
    """Generate index.html for a directory"""
    dir_path = Path(directory)
    
    # Get relative path from html root
    try:
        rel_path = dir_path.relative_to('/var/www/html')
        title = str(rel_path) + '/' if str(rel_path) != '.' else ''
    except ValueError:
        title = ''
    
    # Collect entries
    folders = []
    files = []
    
    try:
        for item in sorted(dir_path.iterdir()):
            if should_exclude(item.name):
                continue
            
            if item.is_dir():
                _, mtime = get_file_info(item)
                folders.append((item.name, mtime))
            elif item.is_file():
                size, mtime = get_file_info(item)
                files.append((item.name, mtime, size))
    except PermissionError:
        pass
    
    # Generate HTML with embedded dark theme styles
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style type="text/css">
* {{ margin: 0; padding: 0; font: inherit; color: inherit; box-sizing: border-box; }}
::selection {{ background: #ddd; color: #000 }}
:root {{ --lh: 1.5em }}
html {{ margin: 0 0 0 calc(100vw - 100%); -webkit-text-size-adjust: 100%; height: 100%; }}
body {{ font: 1em/var(--lh) monospace; padding: 16vh 2em 0; background: #f2f2f2; display: grid; grid: 1fr / minmax(auto, 64ch); justify-content: center; height: 100%; }}
a {{ display: inline-block; text-decoration: none; padding: .16666em; margin-left: -.16666em; }}
a i {{ border-bottom: 1px dotted }}
a:active i {{ border: none }}
footer {{ padding: calc(var(--lh) * 2) 0 8vh; display: flex; justify-content: space-between; align-items: center; }}
h1,p {{ margin-bottom: var(--lh); }}
table {{ border: none; margin-top: -.16666em }}
td:first-child {{ padding: 0 }}
td {{ padding: 0 3em }}
tr td:last-child {{ padding: 0}}
.theme-toggle {{ cursor: pointer; border: 1px solid #000; padding: 4px 8px; font-size: 0.9em; background: transparent; transition: all 0.2s; }}
.theme-toggle:hover {{ background: #ddd; }}

/* Dark theme */
body.dark {{ background: #1a1a1a; color: #e0e0e0; }}
body.dark ::selection {{ background: #333; color: #fff; }}
body.dark a i {{ border-color: #666; }}
body.dark .theme-toggle {{ border-color: #e0e0e0; }}
body.dark .theme-toggle:hover {{ background: #333; }}

@media (max-device-width: 600px) {{
  body {{ padding-top: 2em; justify-content: start }}
  footer {{ padding: 2em 0; flex-direction: column; gap: 1em; align-items: flex-start; }}
  a i {{ border-color: #888 }}
}}
</style>
<title>{title if title else 'files/'}</title>
</head>
<body>
<main>
<h1>{title if title else 'files/'}</h1>
<p>-</p>
<table cellpadding=0 cellspacing=0 cols=3>
<tbody>
"""
    
    # Add folders
    for name, mtime in folders:
        html += f'<tr><td><a href="{name}/"><i>{name}/</i></a><td><time>{mtime}</time><td align=right>-\n'
    
    # Add files
    for name, mtime, size in files:
        html += f'<tr><td><a href="{name}"><i>{name}</i></a><td><time>{mtime}</time><td align=right>{size}\n'
    
    html += """</table>
</main>
<footer>
<a href="../"><i>../</i></a>
<button class="theme-toggle" onclick="toggleTheme()">◐</button>
</footer>
<script>
function toggleTheme() {
  location.hash = location.hash === '#dark' ? '' : '#dark';
}
if (location.hash === '#dark') document.body.classList.add('dark');
</script>
</body>
</html>"""
    
    return html

def generate_all(root_dir):
    """Generate index.html files for all directories"""
    root_path = Path(root_dir)
    
    for dirpath, dirnames, filenames in os.walk(root_path):
        # Filter out excluded directories
        dirnames[:] = [d for d in dirnames if not should_exclude(d)]
        
        current_dir = Path(dirpath)
        
        # Generate single index.html with dark theme support
        html = generate_html(current_dir)
        with open(current_dir / 'index.html', 'w') as f:
            f.write(html)
        
        print(f"Generated index for: {current_dir}")

if __name__ == '__main__':
    print("Generating directory indexes...")
    generate_all('/var/www/html')
    print("Generation complete!")
