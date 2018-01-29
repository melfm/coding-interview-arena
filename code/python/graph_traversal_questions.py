"""Graph traversal questions."""


def dfs(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            neighbors = graph[node]

            for neighbor in neighbors:
                stack.extend(neighbor)

    return visited


def bfs(graph, start_node):
    visited = []
    queue = [start_node]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbors = graph[node]

            for neighbor in neighbors:
                queue.append(neighbor)
    return visited
