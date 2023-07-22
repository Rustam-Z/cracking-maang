def fib(n):
    # A naive recursive solution.
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result


def _fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = _fib_2(n-1, memo) + _fib_2(n-2, memo)
    memo[n] = result
    return result


def fib_memo(n):
    # A memoized solution.
    memo = [None] * (n + 1)
    return _fib_2(n, memo)


def fib_bottom_up(n):
    # A bottom-up solution
    if n == 1 or n == 2:
        return 1

    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]

    return bottom_up[n]
