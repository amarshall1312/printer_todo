from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import generate_png as gp
import bit_png as ipr

import generate_html as gh

from print_receipt import print_receipt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

def run_pipeline(data: dict):
    gh.render_receipt(data, "output/html/pipeline_test.html")
    gp.html_file_to_png("output/html/pipeline_test.html", "output/png/")
    ipr.convert_for_thermal("output/png/pipeline_test.png", "output/png/pipeline_1bit.png")
    print_receipt("output/png/pipeline_1bit.png")



@app.post("/request")
def handle_request(data: dict):
    print("hello from post")
    run_pipeline(data)
    
    return {
        "success": True,
        "received": data
    }
