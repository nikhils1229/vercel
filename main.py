from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List

app = FastAPI()

# Enable CORS for all origins and methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks data from file
with open("marks.json") as f:
    marks_data = json.load(f)

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    return {"marks": [marks_data.get(n, None) for n in name]}
