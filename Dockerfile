FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/

# Create credentials directory
RUN mkdir -p /app/credentials

# Set working directory to src for proper imports
WORKDIR /app/src

# Expose port for HTTP transport
EXPOSE 3001

# Default command
CMD ["python", "main.py"]
