from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modèle pour la requête JSON
class SentimentRequest(BaseModel):
    text: str

@app.get("/status")
def read_status():
    return {"status": "ok"}

@app.get("/permissions")
def get_permissions(username: str, password: str):
    if username == "valid_user" and password == "password":
        return {"permissions": "full access"}
    else:
        raise HTTPException(status_code=403, detail="Forbidden")

@app.post("/v1/sentiment")
def sentiment_v1(data: SentimentRequest):
    text = data.text
    sentiment_score = 1 if "love" in text.lower() else -1
    return {"score": sentiment_score}

@app.post("/v2/sentiment")
def sentiment_v2(data: SentimentRequest):
    text = data.text
    sentiment_score = -1 if "hate" in text.lower() else 1
    return {"score": sentiment_score}

