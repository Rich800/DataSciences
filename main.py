from fastapi import FastAPI

app = FastAPI()

# Définir la route /status
@app.get("/status")
def read_status():
    return {"status": "ok"}

