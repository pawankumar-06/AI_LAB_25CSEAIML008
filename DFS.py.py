#dfs{Depth First Search }
def dfs(graph, start_node):
    visited = []
    stack = [start_node]   # Stack

    while stack:
        current_node = stack.pop()   # Remove from end (LIFO)

        if current_node not in visited:
            print("Exploring node:", current_node)
            visited.append(current_node)

            # Push neighbors onto the stack
            for neighbor in reversed(graph.get(current_node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited


print("--- Build Your Graph ---")

student_graph = {}

num_edges = int(input("How many edges? "))

for i in range(num_edges):
    u, v = input(f"Edge {i + 1}: ").split()

    if u not in student_graph:
        student_graph[u] = []

    if v not in student_graph:
        student_graph[v] = []

    student_graph[u].append(v)
    student_graph[v].append(u)

start = input("Enter starting node: ")

print(student_graph)

result = dfs(student_graph, start)

print("Visited:", result)