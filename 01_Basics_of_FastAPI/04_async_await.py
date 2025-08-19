import asyncio
from fastapi import FastAPI, HTTPException

app = FastAPI()

# create a method
@app.get("/wait")
async def main():
    await asyncio.sleep(3)
    return {"message" : "waiting is finished"}
    