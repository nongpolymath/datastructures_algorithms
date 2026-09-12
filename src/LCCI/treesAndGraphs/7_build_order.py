"""
Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of projects, 
where the second project is dependent on the first project). All of a project's dependencies must be built before the project is. 
Find a build order that will allow the projects to be built. If there is no valid build order, return an error. 
EXAMPLE Input: projects: a, b, c, d, e, f dependencies: (a, d), (f, b), (b, d), (f, a), (d, c) Output: f, e, a, b, d, c
BFS — Kahn's algorithm (the intuitive one)
1. Build the graph and compute each node's in-degree (number of prerequisites it still needs).
2. Put all nodes with in-degree 0 (no prerequisites) into a queue — you can take these right away.
3. Pop a node, "take" it, and decrement the in-degree of everything it unlocks. If a neighbor's in-degree hits 0, it's now unlocked — push it into the queue.
4. If you eventually process every node, there's no cycle. If some nodes are never unlocked (still have prerequisites nobody removed), 
    they're stuck in a cycle.
"""

from collections import deque


def find_order_bfs(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    for course , pre in prerequisites:
        graph[course].append(pre)
        indegree[course] +=1
    queue = deque(c for c in range(num_courses) if indegree[c]==0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return order if len(order) == num_courses else []


def can_finish_bfs(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """Kahn's algorithm: repeatedly remove nodes with in-degree 0."""
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    for course, pre in prerequisites:
        graph[course].append(pre)
        indegree[course] +=1
    queue = deque(c for c in range(num_courses) if indegree[c] == 0)
    taken = 0
    while queue:
        node = queue.popleft()
        taken += 1
        for nxt in graph[node]:
            indegree[nxt] -=1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return taken == num_courses

