import logging
import os

def log_order(response):
    with open("logs/order_log.txt", "a") as log_file:
        log_file.write(str(response) + "\n")

LOG_PATH = os.path.join("logs", "order_log.txt")
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(msg):
    logging.info(msg)

def log_error(msg):
    logging.error(msg)
