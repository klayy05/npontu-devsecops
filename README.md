# Npontu Technologies — DevSecOps Intern Assignment

A basic CI/CD pipeline built with GitHub Actions, Docker, and Render.com.

## Stack
- App: Python (Flask)
- Tests: Pytest
- Container: Docker
- CI/CD: GitHub Actions
- Staging: Render.com

## Pipeline Stages

| Stage | What it does |
|-------|-------------|
| Test | Runs pytest against the Flask app |
| Build | Builds and smoke-tests the Docker image |
| Deploy | Triggers a Render.com deploy on every push to main |

## Running Locally

pip install -r requirements.txt
python app.py

## Running Tests

pytest test_app.py -v

## Running with Docker

docker build -t npontu-devsecops-app .
docker run -p 5000:5000 npontu-devsecops-app

## Security
See SECURITY.md for the documented vulnerability and fix.

## Setup: Render Deploy Hook
1. Create a new Web Service on Render.com connected to this repo
2. Copy the Deploy Hook URL from Render dashboard
3. Add it as a GitHub secret named RENDER_DEPLOY_HOOK_URL
