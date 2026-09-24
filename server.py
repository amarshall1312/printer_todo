from fastapi import FastAPI

app = FastAPI()

@app.post("/request")
def handle_request(data: dict):

    
    return {
        "success": True,
        "received": data
    }
