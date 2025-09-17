from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, u, v):
        # Ensure node u exists in the adjacency list
        if u not in self.adj_list:
            self.adj_list[u] = []
        # Ensure node v exists in the adjacency list
        if v not in self.adj_list:
            self.adj_list[v] = []
        
        # Add an edge from u to v
        self.adj_list[u].append(v)
        
        # Add an edge from v to u for an undirected graph
        self.adj_list[v].append(u)  # For undirected graph

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            # Remove the vertex itself
            del self.adj_list[vertex]
            # Remove all edges pointing to this vertex from other vertices
            for other_vertex in self.adj_list:
                self.adj_list[other_vertex] = [v for v in self.adj_list[other_vertex] if v != vertex]

    def remove_edge(self, u, v):
        if u in self.adj_list and v in self.adj_list:
            # Remove edge from u to v
            if v in self.adj_list[u]:
                self.adj_list[u].remove(v)
            # Remove edge from v to u (for undirected graph)
            if u in self.adj_list[v]:
                self.adj_list[v].remove(u)


    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.adj_list.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result
    
    def dfs(self, start):
        visited = set()
        stack = [start]
        result = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                # For DFS, we typically add neighbors in reverse order
                # to process them in a more "natural" left-to-right order
                # if the adjacency list is ordered.
                # Or simply iterate and let the stack handle the order.
                # Complexity is O(V+E)
                for neighbor in reversed(self.adj_list.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result
