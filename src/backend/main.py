from fastapi import FastAPI
from models import Graph
from topologicalSort import main as sortByTopologicalSort
from mergeSort import mergeSort as sortByMergeSort
from quickSort import quickSort as sortByQuickSort

app = FastAPI()

@app.get("/")
def root():
    return {"Hello World!"}

@app.post("/topologicalSort")
def topologicalSort(data: Graph)-> list[int]:
    return sortByTopologicalSort(data.graph)

@app.post("/mergeSort")
def mergeSort(data: Graph)-> list[int]:
    ot = sortByTopologicalSort(data.graph)
    return sortByMergeSort(ot)

@app.post("/quickSort")
def quickSort(data: Graph)-> list[int]:
    ot = sortByTopologicalSort(data.graph)
    return sortByQuickSort(ot)
