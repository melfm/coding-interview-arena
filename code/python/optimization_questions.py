"""Questions that require optimization tricks."""

import time


def sum_set_of_k_v1(k):
    """Write a function to return consecutive subset of numbers
    that sum to K. For instance, sum(10) -> {(1+2+3+4)},
    sum(9) ->{(2+3+4),(4+5)}.
    Q: How can you optimize the run-time?
    """

    total_set = []
    current_set = []
    current_sum = 0

    # Optimization no.1-> Only need to check the sum
    # for half/k as the sum will be larger.
    start = time.time()
    for p1 in range(1, int(k/2) + 1):
        p2 = p1 + 1

        current_sum = p1
        current_set.append(p1)

        while(current_sum < k):
            current_sum += p2
            current_set.append(p2)
            p2 += 1

            if current_sum == k:
                # Found a sum, reset vars
                total_set.append(current_set)
                current_set = []
                current_sum = 0
                break

        if current_sum > k:
            # Didn't find a sum, and current_sum is too large.
            current_sum = 0
            current_set = []

    end = time.time()
    print('Total time v1 ', end - start)
    return total_set
