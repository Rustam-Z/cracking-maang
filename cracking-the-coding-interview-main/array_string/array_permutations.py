"""
Problem: Given the array of integers, return all permutations with these numbers.
    Input: array of integers.
    Output: array containing all permutations.

Example:
    Input: [1, 2, 3]
    Output: [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]
"""


def permute(nums: list[int]) -> list[list[int]]:
    res = []

    # base case
    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)

        res.extend(perms)

        nums.append(n)  # As we are removing the n, we have to add it again.

    return res


def main():
    nums = [1, 2, 3]
    ans = permute(nums)
    print(ans)  # [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]


if __name__ == "__main__":
    main()
