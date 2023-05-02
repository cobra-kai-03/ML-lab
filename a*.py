def astar(start_node, goal_node, h_func, successors_func):
    """ A* search algorithm implementation """
    
    # The list stores nodes ordered by f_score (f_score = g_score + h_score)
    queue = [(h_func(start_node, goal_node), start_node)]
    
    # The dictionary stores the best known g_score for each node
    g_scores = {start_node: 0}
    
    # The dictionary stores the parent of each node in the optimal path
    parents = {start_node: None}
    
    while queue:
        # Get the node with the lowest f_score
        current_f_score, current_node = min(queue)
        queue.remove((current_f_score, current_node))
        
        if current_node == goal_node:
            # We found the optimal path
            path = []
            while current_node:
                path.append(current_node)
                current_node = parents[current_node]
            path.reverse()
            return path
        
        for successor_node in successors_func(current_node):
            # Compute the tentative g_score for the successor_node
            tentative_g_score = g_scores[current_node] + 1
            
            if successor_node not in g_scores or tentative_g_score < g_scores[successor_node]:
                # We found a better path to the successor_node
                g_scores[successor_node] = tentative_g_score
                f_score = tentative_g_score + h_func(successor_node, goal_node)
                queue.append((f_score, successor_node))
                parents[successor_node] = current_node
                queue.sort()
    
    # No path found
    return None

# Example usage with user input

# Get the start node, goal node, and graph from the user
start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")
graph = {}

while True:
    edge = input("Enter an edge (node1,node2,weight) or press Enter to finish: ")
    if not edge:
        break
    node1, node2, weight = edge.split(',')
    weight = int(weight)
    if node1 not in graph:
        graph[node1] = {}
    graph[node1][node2] = weight

# Get the heuristics from the user
heuristics = {}
for node in graph:
    heuristics[node] = int(input(f"Enter the heuristic value for {node}: "))

# Define the successors function for the graph
def successors_func(node):
    return graph.get(node, {}).keys()

# Define the heuristic function for A* search
def h_func(node, goal_node):
    return heuristics[node]

# Run A* search and print the result
path = astar(start_node, goal_node, h_func, successors_func)
if path:
    print("Optimal path:", ' -> '.join(path))
else:
    print("No path found.")
