from typing import List, Dict
from app.pipeline import Node, Edge

def is_dag(nodes: List[Node], edges: List[Edge]) -> bool:
    graph: Dict[str, List[str]] = {node.id: [] for node in nodes}

    for edge in edges:
        # safety: ignore invalid edges
        if edge.source in graph:
            graph[edge.source].append(edge.target)

    visited = set()
    rec_stack = set()

    def dfs(node: str) -> bool:
        if node in rec_stack:
            return True
        if node in visited:
            return False

        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True

        rec_stack.remove(node)
        return False

    for node in graph:
        if dfs(node):
            return False

    return True