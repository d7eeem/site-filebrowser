# Site FileBrowser

A beautiful, minimalist file browser with automatic directory indexing and dark/light theme support. Perfect for showcasing files, documents, images, and content with a clean, retro-inspired aesthetic.

![Docker Build](https://github.com/d7eeem/site-filebrowser/actions/workflows/docker-publish.yml/badge.svg)

> **⚡ Vibe Coded**  
> This project was entirely vibe-coded through an AI conversation - from concept to deployment. No traditional coding session, just pure conversational development. The power of Claude + human imagination! 🤖✨

## ✨ Features

- 🎨 **Minimal Aesthetic** - Clean, monospace design inspired by classic directory listings
- 🌓 **Dark/Light Themes** - Toggle between themes with persistent preference (URL hash)
- 🔄 **Auto-Regeneration** - Automatically detects file changes and updates indexes
- 📁 **Recursive Indexing** - Generates beautiful listings for all directories
- 📊 **File Metadata** - Displays file sizes and modification dates
- 🚫 **Smart Exclusions** - Automatically hides system files and build artifacts
- 🐳 **Fully Dockerized** - One command to run anywhere
- 🚀 **CI/CD Ready** - Automatic builds via GitHub Actions
- 📱 **Responsive** - Works beautifully on mobile and desktop
- ⚡ **Lightweight** - Minimal dependencies, fast performance

## 🚀 Quick Start

### Using Docker Compose (Recommended)

```bash
# Clone the repository
git clone https://github.com/d7eeem/site-filebrowser.git
cd site-filebrowser

# Create content directory and add files
mkdir -p html/posts html/images
echo "Hello World" > html/posts/welcome.txt

# Start the server
docker-compose up -d

# Access at http://localhost:8800
```

### Using Docker Run

```bash
docker run -d \
  -p 8800:80 \
  -v $(pwd)/html:/var/www/html \
  --name site-filebrowser \
  ghcr.io/d7eeem/site-filebrowser:latest
```

### From Source

```bash
# Build the image
docker build -t site-filebrowser .

# Run
docker run -d -p 8800:80 -v $(pwd)/html:/var/www/html site-filebrowser
```

## 📁 Directory Structure

```
site-filebrowser/
├── .github/
│   └── workflows/
│       └── docker-publish.yml    # CI/CD pipeline
├── html/                          # Your content goes here
│   ├── style.css                  # Global stylesheet
│   ├── template.html              # Page template
│   ├── posts/                     # Blog posts, articles
│   ├── images/                    # Images, photos
│   └── projects/                  # Project files
├── Dockerfile                     # Container definition
├── compose.yml                    # Docker Compose config
├── generator.py                   # Index generator
├── watcher.sh                     # File watcher
├── nginx.conf                     # Nginx configuration
├── new-page.sh                    # Page creation script (Bash)
├── new-page.py                    # Page creation script (Python)
└── README.md                      # This file
```

## 📝 Creating Content

### Adding Files

Simply add files to the `html/` directory:

```bash
# Add a document
cp ~/document.pdf html/documents/

# Add an image
cp ~/photo.png html/images/

# Indexes regenerate automatically!
```

### Creating HTML Pages

#### Using the Scripts

**Bash:**
```bash
./new-page.sh "My Blog Post" posts/my-post.html
```

**Python:**
```bash
python3 new-page.py "About Me" about.html
```

#### Manual Method

```bash
# Copy template
cp html/template.html html/posts/my-new-post.html

# Edit content
nano html/posts/my-new-post.html
```

Update the title, heading, and content between the `<main>` tags.

### Page Template Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Your Title</title>
<link rel="stylesheet" href="/style.css">
</head>
<body>
<main>
<h1>Your Title</h1>
<p>-</p>

<!-- Your content here -->

<time>2026-01-18</time>
</main>
<footer>
<p><a href="../"><i>../</i></a></p>
<button class="theme-toggle" onclick="toggleTheme()">◐</button>
</footer>
<script>
function toggleTheme() {
  location.hash = location.hash === '#dark' ? '' : '#dark';
}
if (location.hash === '#dark') document.body.classList.add('dark');
</script>
</body>
</html>
```

## 🎨 Theming

### Toggle Theme

Click the **◐** button in the footer to switch between light and dark themes.

### Theme Persistence

The theme preference is stored in the URL hash:
- Light mode: `http://localhost:8800/`
- Dark mode: `http://localhost:8800/#dark`

Share links with `#dark` to open directly in dark mode!

### Customizing Styles

Edit `html/style.css` to customize:
- Colors and backgrounds
- Fonts and spacing
- Layout and grid
- Mobile breakpoints

## ⚙️ Configuration

### Change Port

Edit `compose.yml`:
```yaml
ports:
  - "8080:80"  # Change 8800 to your desired port
```

### Exclude Additional Files

Edit `generator.py` and modify `EXCLUDE_PATTERNS`:
```python
EXCLUDE_PATTERNS = {
    '.git', 'node_modules', '.DS_Store', 
    '__pycache__', '.env',
    'index.html',
    'style.css', 'template.html',
    'new-page.sh', 'new-page.py',
    '.gitignore', 'README.md',
    'YOUR_PATTERN_HERE'  # Add your exclusions
}
```

### Custom Timezone

Edit `compose.yml`:
```yaml
environment:
  - TZ=America/New_York  # Change timezone
```

## 🐳 Docker Commands

```bash
# Start
docker-compose up -d

# Stop
docker-compose down

# View logs
docker-compose logs -f

# Restart
docker-compose restart

# Rebuild after code changes
docker-compose up -d --build

# Force regenerate indexes
docker-compose exec file-browser python3 /app/generator.py

# Shell access
docker-compose exec file-browser sh
```

## 🚀 Deployment

### GitHub Container Registry

The project includes automated CI/CD via GitHub Actions. Every push to `main`/`master` automatically builds and publishes to GitHub Container Registry.

```bash
# Pull from registry
docker pull ghcr.io/d7eeem/site-filebrowser:latest

# Run
docker-compose pull
docker-compose up -d
```

See [CI/CD Documentation](README-CICD.md) for complete setup instructions.

### Production Deployment

1. **Clone repository on server:**
```bash
git clone https://github.com/d7eeem/site-filebrowser.git
cd site-filebrowser
```

2. **Add your content:**
```bash
# Upload files via SCP, rsync, or git
rsync -avz ~/my-content/ html/
```

3. **Start container:**
```bash
docker-compose up -d
```

4. **Update content:**
```bash
# Add files to html/ directory
# Indexes regenerate automatically
```

5. **Update to latest version:**
```bash
git pull
docker-compose pull
docker-compose up -d
```

### Reverse Proxy (Nginx/Caddy)

**Nginx:**
```nginx
server {
    listen 80;
    server_name files.example.com;
    
    location / {
        proxy_pass http://localhost:8800;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

**Caddy:**
```
files.example.com {
    reverse_proxy localhost:8800
}
```

## 🛠️ Development

### Project Structure

- **generator.py** - Scans directories and generates HTML indexes
- **watcher.sh** - Monitors filesystem changes using inotify
- **nginx.conf** - Web server configuration
- **Dockerfile** - Multi-layer container build
- **compose.yml** - Docker Compose orchestration

### Local Development

```bash
# Make changes to generator.py
vim generator.py

# Rebuild container
docker-compose up -d --build

# Test changes
curl http://localhost:8800
```

### Running Generator Manually

```bash
# Inside container
docker-compose exec file-browser python3 /app/generator.py

# Outside container (requires Python 3)
python3 generator.py
```

## 🧪 Testing

```bash
# Test file creation
echo "test" > html/test.txt
sleep 2
curl http://localhost:8800 | grep "test.txt"

# Test directory creation
mkdir html/test-dir
sleep 2
curl http://localhost:8800 | grep "test-dir"

# Test index generation
docker-compose exec file-browser python3 /app/generator.py
ls html/index.html
```

## 📊 Performance

- **Build time:** ~30 seconds
- **Index generation:** <1 second for 100 files
- **Memory usage:** ~50MB
- **Image size:** ~50MB (Alpine-based)
- **Response time:** <10ms (static files)

## 🐛 Troubleshooting

### Files not appearing?

```bash
# Check file permissions
ls -la html/

# Verify exclusion patterns
grep EXCLUDE_PATTERNS generator.py

# Check container logs
docker-compose logs -f

# Manually regenerate
docker-compose exec file-browser python3 /app/generator.py
```

### Theme toggle not working?

- Clear browser cache
- Check JavaScript console for errors
- Verify `style.css` is loaded
- Ensure URL hash is preserved

### Port already in use?

```bash
# Check what's using the port
lsof -i :8800

# Change port in compose.yml
vim compose.yml  # Edit ports section
```

### Container won't start?

```bash
# Check Docker status
docker ps -a

# View container logs
docker logs site-filebrowser

# Rebuild from scratch
docker-compose down
docker-compose up -d --build
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Design inspired by classic Unix directory listings
- Aesthetic inspired by [williamjansson.com](https://williamjansson.com)
- Built with minimal dependencies for maximum simplicity
- **100% vibe-coded** - Developed entirely through conversational AI without writing code manually
- Powered by Claude (Anthropic) - Proof that good vibes make good code ✨

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/d7eeem/site-filebrowser/issues)
- **Discussions:** [GitHub Discussions](https://github.com/d7eeem/site-filebrowser/discussions)

## 🔗 Links

- **GitHub:** https://github.com/d7eeem/site-filebrowser
- **Container Registry:** https://ghcr.io/d7eeem/site-filebrowser
- **Documentation:** [README-CICD.md](README-CICD.md)

---

**Built with ❤️ for simplicity and minimalism**
