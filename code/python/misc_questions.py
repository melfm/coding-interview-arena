

def isPowerOf3_loop(n):

    if n < 1:
        return False

    while(n % 3 == 0):
        n /= 3

    return n == 1


def isPowerOf3_int_limit(n):
    # Works for integers of limited size
    # The biggest power of 3 that fits into
    # signed 32 bits (3^19)
    return n > 0 and 1162261467 % n == 0


def isPowerOf3_recursive(n):

    if n < 1:
        return False

    if n == 1:
        return True

    return isPowerOf3_recursive(n/3)
