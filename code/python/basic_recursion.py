# Basic recursive functions


def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n-1)


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


def fib_loop(n):

    a, b = 0, 1

    seq = []
    seq.append(a)
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
        seq.append(a)

    print(seq)


def mult_3(n):
    if n == 1:
        return 3
    else:
        multiple = mult_3(n - 1) + 3
        print(multiple)
        return multiple


def sum_first_n(n):
    if n == 0:
        return 0
    return n + sum_first_n(n - 1)


def pascal_tri(n):
    if n == 1:
        return [[1]]
    else:
        new_row = [1]
        triangle = pascal_tri(n - 1)
        last_row = triangle[-1]
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        triangle.append(new_row)
    return triangle


if __name__ == '__main__':
    print('Factorial', factorial(12))
    print('Fibonacci recursive', fib(6))

    print('Fibonacci sequence:')
    fib_loop(6)

    print('Multiples of 3 ->')
    mult_3(9)

    print('Sum of first N ->', sum_first_n(5))
    print('Pascal triangle')
    print(pascal_tri(6))
