FROM nginx:alpine

# Install Python and inotify-tools
RUN apk add --no-cache \
    python3 \
    py3-pip \
    inotify-tools \
    bash

# Create app directory
RUN mkdir -p /app

# Copy scripts
COPY generator.py /app/
COPY watcher.sh /app/
COPY nginx.conf /etc/nginx/nginx.conf

# Make scripts executable
RUN chmod +x /app/watcher.sh /app/generator.py

# Create html directory
RUN mkdir -p /var/www/html

# Expose port
EXPOSE 80

# Create entrypoint script
RUN echo '#!/bin/bash' > /entrypoint.sh && \
    echo '/app/watcher.sh &' >> /entrypoint.sh && \
    echo 'nginx -g "daemon off;"' >> /entrypoint.sh && \
    chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
