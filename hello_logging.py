import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Configure logging
logging.basicConfig(filename="app.log", filemode="w", format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

try:
    # Some code that may raise an exception
    result = 1 / 0
except Exception as e:
    logger.exception("An error occurred: %s", e)
