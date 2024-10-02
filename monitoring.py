import logging
from flask import request
from logging_loki import LokiHandler

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Loki configuration
loki_handler = LokiHandler(
    url="http://localhost:3100/loki/api/v1/push",  # Adjust the URL to your Loki instance
    tags={"application": "flask-app"},
    version="1",
)
logger.addHandler(loki_handler)

def log_request():
    logger.info(f"Request: {request.method} {request.url} - Body: {request.json}")

def log_response(response):
    logger.info(f"Response: {response.status_code} - Body: {response.get_data(as_text=True)}")
    return response
