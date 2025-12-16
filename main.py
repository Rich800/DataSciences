from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

@app.get("/permissions")
def get_permissions(username: str, password: str):
    if username == "valid_user" and password == "password":
        return {"permissions": "full access"}
    else:
        raise HTTPException(status_code=403, detail="Forbidden")

