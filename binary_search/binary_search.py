def binary_search(nums, target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (right + left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1

    return -1


def search_in_rotated_sorted_array(nums, target: int) -> int:
    """
    https://leetcode.com/problems/search-in-rotated-sorted-array/

    Given the array nums after the possible rotation and an integer target,
    return the index of target if it is in nums,
    or -1 if it is not in nums.

    SOLUTION #1
    1. Change the array by finding the rotation point
    2. Apply binary search

    SOLUTION #2
    1. Find rotation point
    2. Modify binary search algorithm
    """
    def find_rotation_point(nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return left

    rotation_point = find_rotation_point(nums)

    if nums[rotation_point] == target:
        return rotation_point
    elif nums[rotation_point] < target <= nums[-1]:
        return binary_search(nums[rotation_point:], target) + rotation_point
    else:
        return binary_search(nums[:rotation_point], target)


def binary_search_recursive(nums, l, r, x):
    # Check base case
    if r >= l:
        mid = l + (r - l) // 2
        if nums[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif nums[mid] > x:
            return binary_search_recursive(nums, l, mid - 1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binary_search_recursive(nums, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    result = binary_search_recursive(arr, 0, len(arr) - 1, x)
    if result != -1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")
