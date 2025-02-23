""" Heap Questions.
"""
import heapq



import heapq

def min_obstacles_to_reach(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    # Priority Queue: (obstacles_removed, row, col)
    # Start with (0 obstacles removed, row=0, col=0)
    min_heap = [(grid[0][0], 0, 0)]
    
    # Distance matrix to track min obstacles removed for each cell
    obstacle_count = [[float('inf')] * cols for _ in range(rows)]
    obstacle_count[0][0] = grid[0][0]
    
    while min_heap:
        removed, r, c = heapq.heappop(min_heap)

        # If we reached the destination, return the number of removed obstacles
        if (r, c) == (rows - 1, cols - 1):
            return removed
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                # If obstacle, increment count
                new_removed = removed + grid[nr][nc]
                
                # If this path is better (fewer obstacles removed), update and continue
                if new_removed < obstacle_count[nr][nc]:
                    obstacle_count[nr][nc] = new_removed
                    heapq.heappush(min_heap, (new_removed, nr, nc))
    # No valid path
    return -1


def find_smallest_range_k_lists(list1, list2, list3):
    """Find the smallest range that includes at least one number from each of the k lists.
        You have k lists of sorted integers.
        Find the smallest range that includes at least
        one number from each of the k lists.

        E.g.
        List1: [4, 10, 15, 24, 26]
        List2: [0, 9, 12, 20]
        List3: [5, 18, 22, 30]

        SL: [20, 24] contains 24 from L2, 20 from L2 and
            22 from L3.

        This is efficient solving with a heap data structure.
        1. initialize smallest_range as MAX_INT
        2. keep 3 pointers/index p1, p2 and p3 which points
            to the first elements of lists L1, L2 and L3
            respectively.
        3. find the max value and min value pointed/indexed
            by p1, p2 and p3
        4. difference of max value and min value discovered
            in step 3 is the current range. Compare it with
            smallest_range and update it, if found smaller.
        5. increment the pointer/index of min value found
            in step 3.
        6. repeat step 3 to 5 until the pointer/index of min
            value is in range.

        constant space and O(n) time.
    """
    
    lists = [list1, list2, list3]
    k = len(lists)
    
    # Min-heap to store (value, list_index, element_index)
    min_heap = []
    
    # Track the maximum value in the heap
    current_max = float('-inf')
    
    # Populate the heap with the first element of each list
    for i in range(k):
        heapq.heappush(min_heap, (lists[i][0], i, 0))
        current_max = max(current_max, lists[i][0])
    
    # Initialize the smallest range variables
    smallest_range = float('inf')
    result_range = None  # Store the range (start, end)
    
    # Process the heap
    while min_heap:
        min_value, list_index, element_index = heapq.heappop(min_heap)
        
        # Update the smallest range if the current range is smaller
        if current_max - min_value < smallest_range:
            smallest_range = current_max - min_value
            result_range = (min_value, current_max)
        
        # Move to the next element in the list that contributed the min_value
        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))
            current_max = max(current_max, next_value)  # Update max value
            
        else:
            break  # If we reach the end of any list, stop
    
    return result_range