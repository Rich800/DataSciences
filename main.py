from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def read_status():
    return {"status": "ok"}

@app.post("/v1/sentiment")
def sentiment_v1(data: dict):
    text = data.get("text")
    # Ajoute ici ta logique d'analyse de sentiment
    return {"sentiment": "positive" if "love" in text else "negative"}

