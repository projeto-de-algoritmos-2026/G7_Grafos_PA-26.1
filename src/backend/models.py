from pydantic import BaseModel

class Graph(BaseModel):
    graph: list[list[int]]