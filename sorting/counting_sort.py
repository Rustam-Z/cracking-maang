"""
Counting sort.

Algorithm:
    1. Find the largest element in the array.
    2. Initialize an array of size max + 1 with all elements 0.
    3. Iterate through the array and store the count of each element in the array.
    4. Store the cumulative sum of each array element.
    5. Find the index of each element of the original array in the count array. This gives the cumulative count.
    6. Place the elements in the output array, decreasing the count by 1 for each element.

Limitations:
    - Only works with non-negative discrete values.
    - Only works with integers.

Time complexity: O(max + size), where max is the largest element, and size is the size of the array.
Space complexity: O(max)
"""


def counting_sort(array):
    # find the largest element in the array
    largest = max(array)

    # create a counting array of size largest + 1
    counting_array = [0] * (largest + 1)

    # store the count of each element at their respective index
    for i in range(len(array)):
        counting_array[array[i]] += 1

    # store the cumulative sum of each array element
    for i in range(1, len(counting_array)):
        counting_array[i] += counting_array[i - 1]

    # find the index of each element of the original array in count array
    # place the elements in the output array
    output = [0] * len(array)
    for i in range(len(array)):
        output[counting_array[array[i]] - 1] = array[i]
        counting_array[array[i]] -= 1

    # As the sort makes inplace operation, copy the sorted elements into the original array
    for i in range(len(array)):
        array[i] = output[i]


if __name__ == '__main__':
    unsorted_array = [0, 4, 20, 11, 2, 2, 0, 8, 3, 3, 1, 13, 100, 0]
    counting_sort(unsorted_array)
    print(unsorted_array)
