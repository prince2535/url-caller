import time
import requests
import logging
import os

# ================= CONFIG =================
TARGET_URL = os.getenv("TARGET_URL")  # Set this in Render dashboard
INTERVAL_SECONDS = 300  # 5 minutes
# =========================================

if not TARGET_URL:
    raise ValueError("TARGET_URL environment variable is not set")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def call_url():
    try:
        response = requests.get(TARGET_URL, timeout=20)
        logging.info(f"URL called | Status: {response.status_code}")
    except Exception as e:
        logging.error(f"Request failed: {e}")

def run_forever():
    logging.info("Worker started. Calling URL every 5 minutes.")
    while True:
        call_url()
        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    run_forever()
