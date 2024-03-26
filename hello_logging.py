import logging

#Create a custom logger
logger = loggin.getLogger(__name__)

# Configure logging
logging.basicConfig(filename="app.log", filemode="w", format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# Log a message
logger.info("Hello, logging world! Custom format.")

