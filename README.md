# Docker GitHub Actions Demo

This repository demonstrates how to build and push a Docker image using GitHub Actions.

## What's Inside

- **Simple HTTP Server**: A Python-based web server that serves a "Hello World" page
- **Alpine Linux Base**: Lightweight Docker image using Alpine Linux
- **GitHub Actions Workflow**: Automated building and pushing to GitHub Container Registry

## Local Development

### Build and Run Locally

```bash
# Build the Docker image
docker build -t hello-world-demo .

# Run the container
docker run -p 8000:8000 hello-world-demo
```

Then visit http://localhost:8000 to see the hello world page.

### Test Without Docker

```bash
# Run the Python server directly
python3 server.py
```

## GitHub Actions Workflow

The workflow (`.github/workflows/docker-build.yml`) automatically:

1. **Triggers** on pushes to main/master branch and pull requests
2. **Builds** the Docker image using the Dockerfile
3. **Pushes** the image to GitHub Container Registry (ghcr.io)
4. **Tests** the built image by running it and making an HTTP request
5. **Tags** images with branch names, PR numbers, commit SHAs, and 'latest' for main branch

## Container Registry

Built images are available at:
```
ghcr.io/[your-username]/[repository-name]:latest
```

## Running the Published Image

```bash
docker run -p 8000:8000 ghcr.io/[your-username]/[repository-name]:latest
```

## Features

- ✅ Lightweight Alpine Linux base image
- ✅ Simple Python HTTP server
- ✅ Automated Docker builds with GitHub Actions
- ✅ Multi-tag strategy (latest, branch, SHA)
- ✅ Basic health check testing
- ✅ GitHub Container Registry integration