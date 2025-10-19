FROM debian:stable-slim

# Install de basic
RUN apt-get update -y

# Install python and uv
RUN apt-get install -y python3 curl
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash -
RUN apt-get install -y nodejs
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy application files and install dependencies
WORKDIR /app
COPY . /app
RUN ~/.local/bin/uv venv && chmod +x .venv/bin/activate && .venv/bin/activate
RUN ~/.local/bin/uv sync
RUN npm install && npm run build
RUN rm -rf node_modules public/components public/shared public/index.html public/index.js public/style.css

RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]