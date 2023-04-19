# A naive recursive solution
# O(2^n) time | O(n) space
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# A memoized solution
# O(n) time | O(n) space
def fib_memoized(n, memoize=None):
    if memoize is None:
        memoize = {1: 1, 2: 1}  # Instead of mutable default
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = fib_memoized(n-1, memoize) + fib_memoized(n-2, memoize)
        return memoize[n]


# A bottom-up solution, we need to save the last two only
# O(n) time | O(1) space
def fib_bottom_up(n):
    last_two = [1, 1]
    counter = 3
    while counter <= n:
        next_fib = sum(last_two)
        last_two[0], last_two[1] = last_two[1], next_fib
        counter += 1
    return last_two[1] if n > 1 else last_two[0]


def main():
    print(fib_bottom_up(6))  # 1 1 2 3 5 8
    print(fib_memoized(6))
    print(fib(6))


if __name__ == "__main__":
    main()
