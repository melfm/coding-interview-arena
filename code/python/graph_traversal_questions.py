"""Graph traversal questions."""
import numpy as np


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


def path_exist(graph,
               start_node,
               node_a,
               node_b,
               visited=[],
               first_node_found=False,
               path_found_list=[]):
    """ Q: You are given a network dataset, composed of nodes
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
                    path_exist(graph, current_node, node_a, node_b, visited,
                               first_node_found, path_found_list)

    return path_found_list


class IslandGraph:
    """
    Finding the number of islands, DFS version.
    This version also assumes adjacent nodes also form connection.
    The orthogonal version is inside `matrix_questions`, and its
    the double loop recursive version.
    """

    def __init__(self, row, col, graph):
        self.row = row
        self.col = col
        self.graph = graph

    def dfs_search(self, visit_map, original_i, original_j):
        """Performs DFS for a 2D matrix.
        """

        stack = []
        num_of_islands = 0

        if self.graph[original_i, original_j] == 1:
            # Increment the counter and visit neighbours
            # only if we encounter an island
            num_of_islands += 1
            stack = [[original_i, original_j]]
        if visit_map[original_i, original_j] == 0:
            visit_map[original_i, original_j] = 1

        while stack:
            node = stack.pop()
            # Update indices
            i = node[0]
            j = node[1]

            # Check the neighbours
            if i < self.row - 1:
                curr_i = i + 1
                if self.graph[curr_i][j] == 1 and \
                        visit_map[curr_i, j] != 1:
                    stack.append([curr_i, j])
                    visit_map[curr_i, j] = 1
            if i != 0:
                curr_i = i - 1
                if self.graph[curr_i][j] == 1 and \
                        visit_map[curr_i, j] != 1:
                    stack.append([curr_i, j])
                    visit_map[curr_i, j] = 1

            if j < self.col - 1:
                curr_j = j + 1
                if self.graph[i][curr_j] == 1 and \
                        visit_map[i, curr_j] != 1:
                    stack.append([i, curr_j])
                    visit_map[i, curr_j] = 1
            if j != 0:
                curr_j = j - 1
                if self.graph[i][curr_j] == 1 and \
                        visit_map[i, curr_j] != 1:
                    stack.append([i, curr_j])
                    visit_map[i, curr_j] = 1

            if i < self.row - 1 and j < self.col - 1:
                curr_i = i + 1
                curr_j = j + 1
                if self.graph[curr_i][curr_j] == 1 and \
                        visit_map[curr_i, curr_j] != 1:
                    stack.append([curr_i, curr_j])
                    visit_map[curr_i, curr_j] = 1

            if i != 0 and j != 0:
                curr_i = i - 1
                curr_j = j - 1
                if self.graph[curr_i][curr_j] == 1 and \
                        visit_map[curr_i, curr_j] != 1:
                    stack.append([curr_i, curr_j])
                    visit_map[curr_i, curr_j] = 1

            if i < self.row - 1 and j != 0:
                curr_i = i + 1
                curr_j = j - 1
                if self.graph[curr_i][curr_j] == 1 and \
                        visit_map[curr_i, curr_j] != 1:
                    stack.append([curr_i, curr_j])
                    visit_map[curr_i, curr_j] = 1

            if i < self.row - 1 and j != 0:
                curr_i = i + 1
                curr_j = j - 1
                if self.graph[curr_i][curr_j] == 1 and \
                        visit_map[curr_i, curr_j] != 1:
                    stack.append([curr_i, curr_j])
                    visit_map[curr_i, curr_j] = 1

        return visit_map, num_of_islands

    def count_islands(self):
        """Returns the number of islands in a given boolean
           island.
        """
        visit_map = np.zeros_like(self.graph)
        num_of_islands_total = 0
        # Visit the cells
        for i in range(0, self.row):
            for j in range(0, self.col):
                if visit_map[i][j] == 1:
                    continue
                visit_map, num_of_islands = self.dfs_search(visit_map, i, j)
                num_of_islands_total += num_of_islands
        return num_of_islands_total


def bfs_node_distance(graph, start_node):
    """Breadth-first search with the added node distance"""

    visited = []
    queue = [start_node]
    distances = {start_node: 0}

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbors = graph[node]

            for neighbor in neighbors:
                if neighbor not in distances:
                    distances[neighbor] = distances[node] + 6

                queue.append(neighbor)

    print('Distances ', distances)
    return [*distances.values()]


def snakes_and_ladder(board, N):
    """
    Given a snake and ladder board, find the minimum number of dice
    throws required to reach the destination X.
    "If I can always roll the die to whatever number I want,
    what would be the least number of rolls to reach the destination?"

    Construct a graph representation of board replacing snakes and
    ladder positions with where in the graph it takes you. Then
    do a BFS search to find the shortest path in the graph.
    Note that with this method, you only pick the forward moves i.e.
    the ladder moves and jump to those.
    """

    class Graph:

        def __init__(self, v=0, dist=0):
            self.v = v
            self.dist = dist

    visited = [False] * N
    queue = []
    visited[0] = True
    queue.append(Graph(0, 0))

    while queue:
        node = queue.pop(0)
        vertex = node.v

        if vertex == N - 1:
            break

        j = vertex + 1

        while (j <= vertex + 6 and j < N):

            if visited[j] == False:

                new_node = Graph()
                new_node.dist = node.dist + 1

                # This logic seems to work for the test example
                # but it feels like its missing something i.e.
                # how do you not go back when you see a snake loc.
                # If you haven't visited it, you always update it to
                # board[j] without considering whether its a ladder
                # or a snake ? Snake node will increase your distance
                # so it wont be the minimum path? Perhaps write a test
                # example that causes this.
                if board[j] != -1:
                    new_node.v = board[j]

                else:
                    new_node.v = j

                queue.append(new_node)
                visited[j] = True

            j += 1

    return node.dist
