from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

import generate_png as gp
import bit_png as ipr

import generate_html as gh

from print_receipt import print_receipt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],

)

def get_db():
    db = sqlite3.connect("../data/receipts.db")
    db.row_factory = sqlite3.Row
    return db

def run_pipeline(data: dict):
    gh.render_receipt(data, "output/html/pipeline_test.html")
    gp.html_file_to_png("output/html/pipeline_test.html", "output/png/")
    ipr.convert_for_thermal("output/png/pipeline_test.png", "output/png/pipeline_1bit.png")
    print_receipt("output/png/pipeline_1bit.png")

@app.get("/categories")
def get_categories():
    db = get_db()
    cursor = db.execute("SELECT category_id, name FROM category ORDER BY name")
    return cursor.fetchall()

@app.get("/subcategories")
def get_subcategories(category_id):
    db = get_db()
    cursor = db.execute(
        """
        SELECT subcategory_id, name
        FROM subcategory
        WHERE category_id = ?
        ORDER BY name
        """,
        (category_id,)
    )
    return cursor.fetchall()

@app.get("/projects")
def get_projects():
    db = get_db()
    cursor = db.execute(
        """
        SELECT project_id, name
        FROM project
        ORDER BY name
        """
    )
    return cursor.fetchall()

@app.post("/request")
def handle_request(data: dict):
    run_pipeline(data)
    
    return {
        "success": True,
        "received": data
    }


