#!/bin/bash

echo "Starting file watcher..."

# Initial generation
python3 /app/generator.py

# Watch for changes and regenerate
while inotifywait -r -e modify,create,delete,move /var/www/html; do
    echo "Change detected, regenerating..."
    python3 /app/generator.py
done
