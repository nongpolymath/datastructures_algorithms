from collections import deque

# graph implementation using adjacency lists
graph_dict1 = {"A": ["B","C"], 
     "B": ["A","D","E"],
     "C": ["A","E"],
     "D": ["B","E","F"],
     "E": ["C","B","D","F"],
     "F": ["D","E"]}

graph_dict2 = {"A":["B","C","D"],
               "B": ["A","E"],
               "C": ["A","D"],
               "D": ["A","C", "E"],
               "E": ["B", "D"]}

class Graph:
    def __init__(self, g_dict=None):
        # Use None as the default and create a new dictionary if one isn't provided.
        # This prevents different graph instances from sharing the same dictionary.
        if g_dict is None:
            self.g_dict = {}
        else:
            self.g_dict = g_dict

    def add_edge(self, vertex1, vertex2):
        # Ensure vertex1 exists in the graph, adding it if not.
        self.add_vertex(vertex1)
        # Ensure vertex2 exists in the graph, adding it if not.
        self.add_vertex(vertex2)
        # Add the edge only if it doesn't already exist to prevent duplicates.
        if vertex2 not in self.g_dict[vertex1]:
            self.g_dict[vertex1].append(vertex2)
        if vertex1 not in self.g_dict[vertex2]:
            self.g_dict[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 not in self.g_dict or vertex2 not in self.g_dict:
            raise ValueError(f"One or both vertices not found in graph")
    
        if vertex1 == vertex2:
            if vertex1 in self.g_dict[vertex1]:
                self.g_dict[vertex1].remove(vertex1)
            return
        if vertex2 in self.g_dict[vertex1]:
            self.g_dict[vertex1].remove(vertex2)
        if vertex1 in self.g_dict[vertex2]:
            self.g_dict[vertex2].remove(vertex1)

    def add_vertex(self, vertex):
        if not vertex in self.g_dict:
            self.g_dict[vertex] = []
            return True
        return False
    
    def remove_vertex(self,vertex):
        if vertex not in self.g_dict:
            raise ValueError(f"Vertex '{vertex}' not found in graph.")
        for v in self.g_dict:
            if vertex in self.g_dict[v]:
                self.g_dict[v].remove(vertex)
        del self.g_dict[vertex]
    
    def print_graph(self):
        for v in self.g_dict:
            print(f"{v} : {self.g_dict[v]}")

    def bfs(self,vertex):
        res = []
        visited = set()
        deq = deque([vertex])
        visited.add(vertex)
        while deq:
            current = deq.popleft()
            for neighbor in self.g_dict[current]:
                if neighbor not in visited:
                    deq.append(neighbor)
                    visited.add(neighbor)
            res.append(current)
        print(" -> ".join(res))

    def dfs(self, vertex):
        result = []
        visited = set()
        visited.add(vertex)
        deq = deque([vertex])
        while deq:
            current = deq.pop()
            result.append(current)
            for v in self.g_dict[current]:
                if v not in visited:
                    deq.append(v)
                    visited.add(v)
        print(" -> ".join(result))

graph = Graph(graph_dict1)
graph.print_graph()
graph.bfs("A")
graph.dfs("A")