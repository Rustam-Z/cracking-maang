"""
Product sum

Problem: the array of given, the array may include another arrays.
You have to sum all elements of array and multiply by its depth level with respect to main array

[1, 2, [3, 4], 5, [6, 7, [8, 9]], 10]
Initially sum = 0 and multiplier = 1

1 + 2 + recursive_sum(3 + 4) + 5 +
+ recursive_sum(6 + 7 + recursive_sum(8 + 9)) +
+ 10

Depth for recursive_sum(3 + 4) and recursive_sum(6 + 7 + recursive_sum(8 + 9)) is 2
But for recursive_sum(8 + 9) depth is 3
"""


# Time: O(N) where N is number of individual numbers
# Space: O(D) where D is the maximum depth in array, it is the recursive call stack space complexity
def product_sum(array, multiplier=1):
    sum = 0
    for i in array:
        if isinstance(i, int):
            sum += i
        if isinstance(i, list):
            sum += product_sum(i, multiplier+1)
    return sum * multiplier


def main():
    test_data = [1, 2, [3, 4], 5, [6, 7, [8, 9]], 10]
    actual = product_sum(test_data)
    assert actual == 160


if __name__ == "__main__":
    main()
