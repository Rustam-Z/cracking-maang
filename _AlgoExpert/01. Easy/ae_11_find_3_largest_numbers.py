"""
https://leetcode.com/problems/third-maximum-number/

Problem: find 3 largest elements in array
NOTE! Don't include duplicates

Solution #1: Create three variables to keep track of 3 largest elements, #NICE
Solution #2: Use heap data structure, #BAD
"""


# O(N) time | O(1) space
def find_3_largest(nums: list) -> list:
    largest = [float("-inf")] * 3
    for num in nums:
        update_largest(largest, num)
    return largest


def update_largest(largest: list, num: int) -> None:
    for i in range(len(largest)-1, -1, -1):
        if num > largest[i]:
            shift_and_update(largest, num, i)
            break  # After we found the place, no need to check further, otherwise will break code

    # INSTEAD OF:
    # if num > largest[2]:
    #     shift_and_update(largest, num, 2)
    # elif num > largest[1]:
    #     shift_and_update(largest, num, 1)
    # elif num > largest[0]:
    #     shift_and_update(largest, num, 0)


def shift_and_update(array: list, num: int, index: int) -> None:
    for i in range(index + 1):
        if i == index:
            array[i] = num
        else:
            array[i] = array[i+1]


def main():
    test_data = [12, 23, 5, 32, 2923, 2, 322, 21]
    actual = find_3_largest(test_data)  # (2923, 322, 32)
    print(actual)


if __name__ == "__main__":
    main()
