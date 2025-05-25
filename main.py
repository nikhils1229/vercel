from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks data (list of dicts)
with open("marks.json") as f:
    marks_list = json.load(f)

# Build a name->marks dictionary for fast lookup
marks_data = {entry["name"]: entry["marks"] for entry in marks_list}

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    return {"marks": [marks_data.get(n, None) for n in name]}
