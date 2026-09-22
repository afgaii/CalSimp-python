import logging
from pathlib import Path


def configure_log():

    log_file = Path("logs/calculator.log")  # log_file = "calculator.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        # 2024-06-15 12:00:00,000 - root - INFO - This is an info message.
        handlers=[
            logging.FileHandler(
                log_file
            ),  # file -> send log messages to a file calculator.log
            logging.StreamHandler(),  # stream -> send log messages to the console/terminal
        ],
        force=True,  # This will override any existing logging configuration
    )
