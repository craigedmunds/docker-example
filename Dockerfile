FROM alpine:latest

# Install Python3 and pip
RUN apk add --no-cache python3 py3-pip

# Create app directory
WORKDIR /app

# Copy the server script
COPY server.py .

# Expose port 8000
EXPOSE 8000

# Run the server
CMD ["python3", "server.py"]