# Deployment guide

## Local Flask
From repository root, install requirements, spaCy model, download dataset, train classifier and run `python app.py`. Open http://127.0.0.1:5000.

## Hosting
A live web URL is optional bonus work. For a public service, use a production WSGI server, set `SECRET_KEY` through environment variables, configure memory/CPU limits for transformer models, use a model cache, add input size limits and authentication/rate limiting as appropriate, disable debug, and verify the deployment against the course checklist. Do not treat the local development server as production-ready.
