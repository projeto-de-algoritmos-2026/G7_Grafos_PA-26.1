from fastapi import FastAPI
from models import Graph
from topologicalSort import main as topologicalSort

app = FastAPI()

@app.get("/")
def root():
    return {"Hello World!"}

@app.post("/topologicalSort")
def read_item(data: Graph)-> list[int]:
    return topologicalSort(data.graph)