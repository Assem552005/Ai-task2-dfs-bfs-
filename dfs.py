def dfs(graph, start, goal):
    visited = {node: False for node in graph}
    parent = {start: None}
    stack = [start]

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            
            if current == goal:
                path = []
                node = current
                while node is not None:
                    path.append(node)
                    node = parent[node]
                path.reverse()
                print("Path found:", path)
                return path
            
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    parent[neighbor] = current
                    stack.append(neighbor)
    
    print("No path found")
    return None

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}
dfs(graph, 0, 4)
