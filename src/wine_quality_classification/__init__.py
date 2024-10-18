import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs" # will create a log folder
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True) #makes the log folder here


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # outputs log to log folder
        logging.StreamHandler(sys.stdout) #prints log in terminal
    ]
)

logger = logging.getLogger("wineclass_logger")