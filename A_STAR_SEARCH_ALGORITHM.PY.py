#A-Star Algorithm Implementation
def get_user_input():
    #1. Take input for Heuristic Values......
    heuristic = {}
    num_nodes = int(input("Enter total number of nodes: "))
    print("\n Enter heuristic values h(n) for each node:")
    for _ in range(num_nodes):
        node = input("Node name: ").strip().upper()
        h_val = float(input(f" heuristic h({node}): "))
        heuristic[node] = h_val


    #2. Take input for Graph Edges......
    graph = {nodes: [] for nodes in heuristic}
    num_edges = int(input("\nEnter total number of directed edges: "))
    print("\nEnter edges in the format (from_node to_node weight):")

    for _ in range(num_edges):
        from_node = input("From node: ").strip().upper()
        to_node = input("To node: ").strip().upper()
        weight = float(input("Weight: "))
        graph[from_node].append((to_node, weight))

    #3. Take input for Graph Edges......
    graph = {nodes: [] for nodes in heuristic}
    num_edges = int(input("\nEnter total number of directed edges: "))
    print("\nEnter edges in the format (from_node to_node weight):")

    for _ in range(num_edges):
        u, v, w = input(f"Edge {_ + 1}: ").strip().upper().split()
        u, v = u.strip(), v.strip()
        weight = float(w)
        graph[u].append((v, weight))

    return  graph, heuristic


    def aster(graph, heuristic, start, goal):
        open_list = [(start, 0 )]  # (node, f(n) = g(n) + h(n))
        came_from = {}
        g_cost = {start: 0}  # g(n) cost from start to node

        while open_list:
            # select node with minimum f = g + h
            current_node = min(open_list, key=lambda x: x[1] + heuristic[x[0]])
            open_list.remove(current)

            current_node = current[0]

            #Goal check and path reconstruction
            if current_node == goal:
                path = []
                while current_node in came_from:
                    current_node = came_from[current_node]
                    path.append(current_node)
                path.reverse()
                return path, g_cost[goal]  # Return reversed path and cost

            
    #Neighbour exploration
            for neighbor, cost in graph.get(current_node, []):
               newcost = g_cost[current_node] + cost

               if neighbor not in g_cost or newcost < g_cost[neighbor]:
                    g_cost[neighbor] = newcost
                    came_from[neighbor] = current_node
                    open_list.append((neighbor, new_Cost))

        return None, float('inf')  # No path found      

            
