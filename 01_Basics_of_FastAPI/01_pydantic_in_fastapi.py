from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    
    
app = FastAPI()

@app.get("/users", response_model = User)
def get_users():
    return (User(id = 1, name = "Bhushan"))