"""Questions that require optimization tricks."""


def sum_set_of_k_v1(k):
    """Write a function to return consecutive subset of numbers
    that sum to K. For instance, sum(10) -> {(1+2+3+4)},
    sum(9) ->{(2+3+4),(4+5)}.
    Q: How can you optimize the run-time?
    """

    total_set = []
    current_set = []
    current_sum = 0

    # Optimization -> Only need to check the sum
    # for half/k as the sum will be larger.
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

    return total_set


def sum_set_of_k_v2(k):
    """Alternative implementation of 'sum_set_of_k_v1'.
    We need to find consecutive numbers that add up to k.
    But we don't know how many consecutive numbers we need.
    So instead of calculating the consecutive sum to find a match,
    we solve the following equation :
        # of sequences : 2
        Equation : n + (n + 1) = 2n + 1
        # of sequences : 3
        Equation : n + (n + 1) + (n + 2) = 3n + 3
        # of sequences : 4
        Equation : 4n + 6

    We can loop through the number of sequences, and solve for the
    above equations. The addition term is always the sum of the sequence
    and the previous term.
    """

    total_set = []
    current_set = []
    addition_term = 1
    for seq in range(2, int(k/2) + 1):
        # Solve for n
        n = (k - addition_term) / seq
        # Only care about positives
        if n > 0:
            # If there is a solution i.e. n is a whole number
            if n.is_integer():
                for x in range(int(n), int(n + seq)):
                    current_set.append(x)
                total_set.append(current_set)
                current_set = []

            addition_term = seq + addition_term

    return total_set
