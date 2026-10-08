# Depth Limited Search (DLS)

def dls(graph, current, goal, limit, path):

    # Add current node to path
    path.append(current)

    # Goal found
    if current == goal:
        return True

    # Depth limit reached
    if limit == 0:
        path.pop()
        return False

    # Visit neighboring nodes
    for neighbor in graph[current]:

        if neighbor not in path:

            if dls(graph, neighbor, goal, limit - 1, path):
                return True

    # Backtracking
    path.pop()
    return False


# ==============================
# MAIN PROGRAM
# ==============================

print("===== DEPTH LIMITED SEARCH =====")

# Number of nodes
n = int(input("Enter number of nodes: "))

graph = {}

# Create nodes
for i in range(n):
    graph[i] = []


# ==============================
# ENTER EDGES
# ==============================

e = int(input("Enter number of edges: "))

print("Enter edges (source destination):")

for i in range(e):

    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)


# ==============================
# INPUT START AND GOAL
# ==============================

start = int(input("Enter starting node: "))
goal = int(input("Enter goal node: "))

limit = int(input("Enter depth limit: "))


# Path list
path = []


# ==============================
# PERFORM DLS
# ==============================

found = dls(graph, start, goal, limit, path)


# ==============================
# DISPLAY RESULT
# ==============================

if found:

    print("\nGoal Found!")

    print("Path:", " -> ".join(map(str, path)))

    print("Depth:", len(path) - 1)

else:

    print("\nGoal not found within the given depth limit.")