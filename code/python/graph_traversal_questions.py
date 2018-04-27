"""Graph traversal questions."""
import pdb

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
               all_paths=[]):
    """ Q1: You are provided with network dataset, composed of nodes
    and one-directional links. Check whether a route exists between
    two specific nodes in the network.
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
                        all_paths.append(path_found)
                        print('Found a path.')

                if current_node in graph:
                    path_exist(graph, current_node, node_a, node_b,
                               visited, first_node_found,
                               all_paths)

    return all_paths


def dfs_possible_routes(graph, node_a, node_b):

    stack = [(node_a, [node_b])]
    #pdb.set_trace()

    while stack:
        #pdb.set_trace()
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == node_b:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def bfs_paths2(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths2(graph, start, goal))
    except StopIteration:
        return None


def path_exist_bfs(graph, start_node, node_a, node_b):

    visited = []
    queue = [start_node]

    first_node_found = False
    no_further_neigh = False

    if start_node == node_a:
        print('Found first node')
        first_node_found = True

    while queue:
        print('Queue ->' ,queue)
        node = queue.pop(0)

        if node == node_a:
            first_node_found = True

        if node not in visited:
            visited.append(node)
            if first_node_found:

                if node == node_b:
                    return True


            if node in graph:
                neighbors = graph[node]
                for neighbor in neighbors:
                    queue.append(neighbor)
            else:
                print('Status of queue ', queue)
                no_further_neigh = True

    return False

