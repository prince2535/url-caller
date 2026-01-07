from fastapi import FastAPI
import threading
from worker import run_forever

app = FastAPI()

@app.get("/")
def health():
    return {"status": "running"}

# Run background worker in separate thread
threading.Thread(target=run_forever, daemon=True).start()
