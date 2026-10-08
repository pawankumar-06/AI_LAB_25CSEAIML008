def bfs(graph,start_node):
    visited =[]
    stack=[start_node]

    while stack:
        current_node=stack.pop()

        if current_node not in visited:
            print(f"Exploring node:{current_node}")
            visited.append(current_node)

            #.get() prevents error if a node has no outing edges
            for neighbour in graph.get(current_node,[]):
                if neighbour not in visited and neighbour not in stack:
                    stack.append(neighbour)
    return visited 

#---User input section---
print("--Build your Graph---")
student_graph={}

#GET the total number of connections
num_edges = int(input("how many edges(connections) does your graph has ?"))
print("enter each edge separted by a space")
for i in range(num_edges):
    #Red the input and split it into two variables
    u,v=input(f"Edge {i+1}:").split()

    #Initialize the lists if the node don,t exist yet
    if u not in student_graph:
        student_graph[u]=[]
    if v not in student_graph:
        student_graph[v]=[]

        #add the connections (Unidirected Graph)
    student_graph[u].append(v)
    student_graph[v].append(u)  

#Get the starting point
start=input("Enter the starting node for the DFS:")

print(f"\nYour Graph Dictionary:{student_graph}")
print("starting BFS traversal...")
bfs(student_graph,start)
                                