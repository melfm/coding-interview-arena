"""Graph traversal questions."""

def dfs(graph, start_node):
    """Depth-first search."""

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

def dfs_recursive(graph, start_node, visited=[]):
    """Depth-first search recursive."""

    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for n in graph[start_node]:
                dfs_recursive(graph, n, visited)


def bfs(graph, start_node):
    """Breadth-first search."""

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
