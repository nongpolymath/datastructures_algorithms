"""
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
1. DFS with Recursion
2. DFS with Stack (Iterative)
3. BFS with DeQue
"""
from collections import defaultdict, deque

def validPathDfsRecurse(n, edges, source, destination):
    """
    :type n: int
    :type edges: List[List[int]]
    :type source: int
    :type destination: int
    :rtype: bool
    """
    if source == destination:
        return True
    graph = defaultdict(list) # adjacency list
    visited = set()
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    def dfs(node):
        if node == destination:
            return True
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                if dfs(nei):
                    return True
        return False
    return dfs(source)


def validPathDfsStack(n, edges, source, destination):
    """
    :type n: int
    :type edges: List[List[int]]
    :type source: int
    :type destination: int
    :rtype: bool
    """
    if source == destination:
        return True
    graph = defaultdict(list) # adjacency list
    visited = set()
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    stack = [source]
    visited.add(source)
    while stack:
        node = stack.pop()
        if node == destination:
            return True
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                stack.append(nei)
    return False

def validPathBfs(n, edges, source, destination):
    """
    :type n: int
    :type edges: List[List[int]]
    :type source: int
    :type destination: int
    :rtype: bool
    """
    if source == destination:
            return True
    graph = defaultdict(list) # adjacency list
    visited = set()
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    q = deque()
    q.append(source)
    visited.add(source)
    while q:
        node = q.popleft()
        if node == destination:
            return True
        for nei in graph[node]:
            if nei not in visited:
                q.append(nei)
                visited.add(nei)
    return False               
