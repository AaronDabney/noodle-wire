from fastapi import FastAPI
from pydantic import BaseModel
from util.pydantic_models import Noodle_Request
import router

app = FastAPI()


@app.get("/")
async def get():
    return {"note": "Processing requests must use POST"}

@app.post("/")
async def post(noodle_request: Noodle_Request):
    print("Debug START")
    print(noodle_request)
    print("Debug STOP")
    try:
        print("Trying")
        result = router.process_request(noodle_request)
    except:
        print("Processor Error")
        return {"Error": "processor error"}
    else:
        return result
