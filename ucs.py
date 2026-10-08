import heapq


# Uniform Cost Search
def ucs(graph, start, goal):

    # Priority queue: (cost, node, path)
    priority_queue = []

    heapq.heappush(priority_queue, (0, start, [start]))

    # Store minimum cost to reach each node
    visited = {}

    while priority_queue:

        # Remove node with lowest cost
        cost, current, path = heapq.heappop(priority_queue)

        # Skip if already visited with lower cost
        if current in visited and visited[current] <= cost:
            continue

        visited[current] = cost

        # Goal found
        if current == goal:
            return path, cost

        # Explore neighbors
        for neighbor, edge_cost in graph[current]:

            new_cost = cost + edge_cost

            new_path = path + [neighbor]

            heapq.heappush(
                priority_queue,
                (new_cost, neighbor, new_path)
            )

    return None, float('inf')


# ==============================
# MAIN PROGRAM
# ==============================

print("===== UNIFORM COST SEARCH =====")

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

print("Enter edges as:")
print("source destination cost")

for i in range(e):

    u, v, cost = map(int, input().split())

    graph[u].append((v, cost))
    graph[v].append((u, cost))


# ==============================
# INPUT START AND GOAL
# ==============================

start = int(input("Enter starting node: "))
goal = int(input("Enter goal node: "))


# ==============================
# PERFORM UCS
# ==============================

path, cost = ucs(graph, start, goal)


# ==============================
# DISPLAY RESULT
# ==============================

if path:

    print("\nGoal Found!")

    print("Optimal Path:", " -> ".join(map(str, path)))

    print("Minimum Cost:", cost)

else:

    print("\nGoal not found.")