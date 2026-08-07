def bfs(graph,start_node):
    visited = []
    queue = [start_node]

    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            print(f"exploring node : {current_node}")
            visited.append(current_node)

            # .get() prevents errors if the node has no outgoing edges
            for neighbor in graph.get(current_node,[]):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

                return visited 

    #---- user input section for a graph-----
print("--- build your graph --")
student_graph = {}

#Get the total number of connections 
num_edges = int(input("how many edges (connections) does your graph have? "))

print("enter edges separated by space (e.g. A B )")
for i in range (num_edges ):
    #read the input and split it into two variables 
    u , v =input(f"Edge (i + 1): ").split()

    #initialize the list  if the nodes don't exist in the graph yet 
    if(u not in student_graph):
        student_graph[u]= []
    if(v not in student_graph):
        student_graph[v]= []

    #get the starting point
start = input("enter the starting node for bfs:")

print(f"\nYour graph dictionary :{student_graph}") 
print("starting bfs traversal ---") 
bfs(student_graph,start) 