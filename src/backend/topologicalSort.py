from typing import Final

FIND: Final = 1 #CONSTANTE GLOBAL
PROCESSED: Final = 2 #CONSTANTE GLOBAL

def topologicalSort(visited: list[int], ot: list[int], graph: list[list[int]], vertice: int) -> bool:
    if visited[vertice] == FIND:
        return False
    if visited[vertice] == PROCESSED:
        return True
    visited[vertice] = FIND
    for adj in graph[vertice]:
        if topologicalSort(visited, ot, graph, adj) == False:
            return False

    visited[vertice] = PROCESSED
    ot.append(vertice)
    return True

def main(graph: list[list[int]]) -> list[int]:
    visited = [0] * len(graph)
    ot = []
    count = 1
    if(len(graph) > 1):
        while count < len(graph):
            if topologicalSort(visited, ot, graph, count) == False:
                ot.clear()
                break
            count += 1

    ot.reverse()
    return ot


