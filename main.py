from fastapi import FastAPI
from pydantic import BaseModel
from src.util.pydantic_models import Noodle_Request
import src.router as router

app = FastAPI()

@app.get("/")
async def get():
    return {"note": "Processing requests must use POST"}

@app.post("/")
async def post(noodle_request: Noodle_Request):
    try:
        result = router.process_request(noodle_request)
    except Exception as e:
        print(f"Processor Error: {str(e)}")
        return {"Error": "Processor Error"}
    else:
        return result
