from collections import deque

# Define the graph as an adjacency list (dictionary)
# Each key represents a person, and its value is a list of people they are connected to.
graph = {}
graph["You"] = ["Alice", "Bob", "Claire"]
graph["Alice"] = ["Peggy"]
graph["Bob"] = ["Anuj", "Peggy"]
graph["Peggy"] = []
graph["Anuj"] = []
graph["Claire"] = ["Thom", "Johnny"]
graph["Thom"] = []
graph["Johnny"] = [] # Added missing initialization for Johnny

def is_mango_seller(person):
    return person.endswith("m")

def mango_seller_bfs(name):
    """
    Implements the Breadth-First Search (BFS) algorithm to find a "mango seller"
    in a social network graph.

    The graph is represented as an adjacency list (dictionary where keys are
    people and values are lists of their direct connections).

    A "mango seller" is defined as a person whose name ends with 'm'.
    """
    # Initialize a deque (double-ended queue) for BFS.
    # It will store the people to be searched.
    search_queue = deque()
    search_queue.extend(graph[name])
    # Keep track of people already searched to avoid infinite loops and redundant processing.
    seen = set()
    while search_queue:
        person = search_queue.popleft()
        
        if not person in seen:  # Check if the current person has already been visited
            if is_mango_seller(person): # check if mango seller or not
                print(f"{person} sells mangoes")
                return True
            else:
                search_queue.extend(graph[person]) # if not mango seller then add more out-neighbors in the search queue
                seen.add(person)
    return False

# breadth_first_search(name="You")

# use Breadth First Search on a rooted tree to list all the files in a directory. trees dont have cycles
from os import listdir
from os.path import isfile, join
from collections import deque

def printnames_bfs(root_dir):
    search_queue = deque()
    search_queue.append(root_dir)
    while search_queue:
        currentdir = search_queue.popleft()
        for file in sorted(listdir(currentdir)):
            fullpath = join(currentdir,file)
            if isfile(fullpath):
                print(fullpath)
            else:
                search_queue.append(fullpath)


# Use Depth first search on a Rooted tree to list all the files in a directory.
def printnames_dfs(dir):
    for file in sorted(listdir(dir)):
        fullpath = join(dir, file)
        if isfile(fullpath):
            print(fullpath)
        else:
            printnames_dfs(fullpath)

printnames_dfs("src")