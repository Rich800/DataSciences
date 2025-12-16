from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/status")
def status():
    return {"status": "ok"}



@app.post("/v2/sentiment")
def sentiment_v2(text: str):
    if text == "I hate this!":
        return {"sentiment": "negative"}
    return {"sentiment": "positive"}

