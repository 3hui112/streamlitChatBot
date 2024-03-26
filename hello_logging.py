import logging

# Configure logging
logging.basicConfig(filename="app.log", filemode="w", format="%(asctime)s - %(message)s", level=logging.INFO)

# Log a message
logging.info("Hello, logging world! Logged to file.")
