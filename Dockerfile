# Use the official Python image
FROM python:3.13-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy dependency files first for better caching
COPY pyproject.toml .
# If you have a lockfile, copy it too:
# COPY uv.lock .

# Install dependencies
RUN uv sync --no-dev

# Copy the rest of the application
COPY . .

# Allow statements and log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED=1
# Default transport for Cloud Run is SSE
ENV TRANSPORT=sse
# Default port for Cloud Run
ENV PORT=8080

# Cloud Run ignores EXPOSE but it's good for local documentation
EXPOSE 8080

# Run the FastMCP server directly using the environment's python
CMD ["python", "server.py"]