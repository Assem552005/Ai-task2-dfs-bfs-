def dfs(graph, start):
    visited = {node: False for node in graph}
    stack = [(start, [start])]

    while stack:
        current, path = stack.pop()
        if not visited[current]:
            print(path)
            visited[current] = True
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    stack.append((neighbor, path + [neighbor]))

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}
dfs(graph, 0)
