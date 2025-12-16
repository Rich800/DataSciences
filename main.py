from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modèle pour la requête JSON
class SentimentRequest(BaseModel):
    text: str

@app.get("/status")
def read_status():
    return {"status": "ok"}

@app.post("/v1/sentiment")
def sentiment_v1(data: SentimentRequest):
    text = data.text
    # Exemple de logique d'analyse de sentiment
    if "love" in text.lower():
        sentiment = "positive"
    else:
        sentiment = "negative"
    return {"sentiment": sentiment}

@app.post("/v2/sentiment")
def sentiment_v2(data: SentimentRequest):
    text = data.text
    # Exemple de logique d'analyse de sentiment pour la version 2
    if "hate" in text.lower():
        sentiment = "negative"
    else:
        sentiment = "positive"
    return {"sentiment": sentiment}

