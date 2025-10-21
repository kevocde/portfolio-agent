FROM debian:stable-slim

ARG VITE_API_URL
ARG VITE_AGENT_NAME
ARG MAX_MESSAGE_LENGTH

# Install de basic
RUN apt-get update -y

# Install python and uv
RUN apt-get install -y python3 curl
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN curl -fsSL https://deb.nodesource.com/setup_current.x | bash - && \
    apt-get clean && \
    apt-get update && \
    apt-get install -y nodejs build-essential
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy application files and install dependencies
WORKDIR /app
COPY . /app
RUN ~/.local/bin/uv venv && chmod +x .venv/bin/activate && .venv/bin/activate
RUN ~/.local/bin/uv sync
# Create a .env file with the environment variables
RUN echo "VITE_API_URL=${VITE_API_URL}" > .env
RUN echo "VITE_AGENT_NAME=${VITE_AGENT_NAME}" >> .env
RUN echo "MAX_MESSAGE_LENGTH=${MAX_MESSAGE_LENGTH}" >> .env
RUN npm install && npm run build
RUN rm -rf node_modules public/components public/shared public/index.html public/index.js public/style.css .env

RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]