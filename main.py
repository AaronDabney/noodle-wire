from fastapi import FastAPI
from pydantic import BaseModel
import router

app = FastAPI()


# Server is started with command `fastapi dev main.py`

# Custom 'types'

class Data_Process_Operation(BaseModel):
    name: str
    parameters: dict

class Data_Process_Request(BaseModel): 
    data: dict
    data_process_operation: Data_Process_Operation


# It's easy to make a GET request on accident. API caller needs to make a POST request.

@app.get("/")
async def get():
    return {"note": "Processing requests must use POST"}


# When a user makes a post request, the json object they send with the request
# gets interpreted as a Data_Process_Request and becomes a real python dict.
# We try to process the request (data_process_request) and deal with an error if it arises.

@app.post("/")
async def post(data_process_request: Data_Process_Request):
    try:
        print("Trying")
        result = router.process_request(data_process_request)
    except:
        print("Processor Error")
        return {"Error": "processor error"}
    else:
        return result

