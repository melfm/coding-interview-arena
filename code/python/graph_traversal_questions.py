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


def path_exist(graph, start_node, node_a, node_b,
               visited=[], first_node_found=False,
               path_found_list=[]):
    """ Q: You are provided with network dataset, composed of nodes
    and one-directional links. Check whether a route exists between
    two specific nodes in the network.

    Args:
        graph: Graph represented as a dict.
        start_node: Root node to start from.
        node_a: First node to start the route.
        node_b: Second node to end the route.
        first_node_found: Set to True when 'node_a' is found.
        path_found_list: Stores the flag which indicates the path
            is found.
    """

    stack = [start_node]

    if start_node == node_a:
        first_node_found = True

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)

            for current_node in graph[start_node]:
                if not first_node_found:
                    if current_node == node_a:
                        first_node_found = True
                if first_node_found:
                    if current_node == node_b:
                        path_found = True
                        current_path = visited
                        current_path.append(current_node)
                        # path = []
                        # path.append(current_path)
                        # print('The paths ', path)
                        path_found_list.append(path_found)

                if current_node in graph:
                    path_exist(graph, current_node, node_a, node_b,
                               visited, first_node_found,
                               path_found_list)

    return path_found_list
