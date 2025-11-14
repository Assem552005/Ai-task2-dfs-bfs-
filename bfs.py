from queue import Queue

def bfs(graph, start, goal):
    q = Queue()
    q.put(start)
    visited = {node: False for node in graph}
    visited[start] = True
    parent = {start: None}

    while not q.empty():
        node = q.get()
        
        if node == goal:
            path = []
            current = node
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            print("Path found:", path)
            return path
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                q.put(neighbor)
    
    print("No path found")
    return None


graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}
bfs(graph, 0, 4)
