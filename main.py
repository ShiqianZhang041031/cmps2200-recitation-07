
def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number.
    counts[i] records how many times fib_recursive(i)
    is called.
    """
    counts[n] += 1

    if n <= 1:
        return n

    return fib_recursive(n - 1, counts) + fib_recursive(n - 2, counts)


def fib_top_down(n, fibs):
    """
    Compute Fibonacci numbers using memoization.
    """
    if fibs[n] != -1:
        return fibs[n]

    if n <= 1:
        fibs[n] = n
    else:
        fibs[n] = fib_top_down(n - 1, fibs) + fib_top_down(n - 2, fibs)

    return fibs[n]


def fib_bottom_up(n):
    """
    Compute Fibonacci numbers using bottom-up
    dynamic programming.
    """
    fibs = [0] * (n + 1)

    if n >= 1:
        fibs[1] = 1

    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]

    return fibs[n]

