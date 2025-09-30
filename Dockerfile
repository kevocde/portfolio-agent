FROM debian:stable-slim

# Install dependencies
RUN apt-get update && \
apt-get install -y curl && \
curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - && \
apt-get install -y nodejs && \
apt-get install -y python3 python3-pip && \
apt-get install -y unzip && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*

# Install uv dependency manager
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

WORKDIR /app

# Copy application files
COPY . /app

# Init venv
RUN ~/.local/bin/uv venv

# Activate venv
RUN . .venv/bin/activate

# Install uv
RUN ~/.local/bin/uv sync

# Install npm dependencies
RUN npm install

# Build the application
RUN npm run build

# Remove npm dependencies
RUN rm -rf node_modules public/components public/shared public/index.html public/index.js public/style.css


RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]