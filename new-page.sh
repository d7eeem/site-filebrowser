#!/bin/bash

# Usage: ./new-page.sh "Page Title" path/to/file.html

if [ $# -lt 2 ]; then
    echo "Usage: ./new-page.sh \"Page Title\" path/to/file.html"
    echo "Example: ./new-page.sh \"My Blog Post\" posts/my-post.html"
    exit 1
fi

TITLE="$1"
FILEPATH="html/$2"
CURRENT_DATE=$(date +%Y-%m-%d)

# Create directory if it doesn't exist
mkdir -p "$(dirname "$FILEPATH")"

# Generate the HTML file
cat > "$FILEPATH" << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>TITLE_PLACEHOLDER</title>
<link rel="stylesheet" href="/style.css">
</head>
<body>
<main>
<h1>TITLE_PLACEHOLDER</h1>
<p>-</p>

<p>Start writing your content here...</p>

<time>DATE_PLACEHOLDER</time>

</main>
<footer>
<p><a href="../"><i>../</i></a></p>
<button class="theme-toggle" onclick="toggleTheme()">◐</button>
</footer>
<script>
function toggleTheme() {
  document.body.classList.toggle('dark');
}
</script>
</body>
</html>
EOF

# Replace placeholders
sed -i "s/TITLE_PLACEHOLDER/$TITLE/g" "$FILEPATH"
sed -i "s/DATE_PLACEHOLDER/$CURRENT_DATE/g" "$FILEPATH"

echo "✓ Created: $FILEPATH"
echo "  Title: $TITLE"
echo "  Date: $CURRENT_DATE"
echo ""
echo "Edit with: nano $FILEPATH"
