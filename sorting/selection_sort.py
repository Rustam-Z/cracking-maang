"""
Selection sort algorithm implementation.

Algorithm:
    1. Find the smallest element in the array.
    2. Swap it with the first element of unsorted part. After each iteration, minimum is placed in the front of the unsorted list.
    3. Repeat the steps above for the rest of the array.

Time Complexity:
    Best O(n^2)
    Worst O(n^2)
    Average O(n^2)
Space Complexity: O(1)
"""


def selection_sort(array):
    for i in range(len(array)):
        min_index = i

        for j in range(i + 1, len(array)):
            # To sort in descending order, change > to < in this line
            # select the minimum element in each loop.
            if array[j] < array[min_index]:
                min_index = j

        # Put min at the correct position.
        array[i], array[min_index] = array[min_index], array[i]
    return array


if __name__ == '__main__':
    unsorted_array = [5, 3, 6, 2, 10, -23, 0]
    selected_array = selection_sort(unsorted_array)  # [-23, 0, 2, 3, 5, 6, 10]
    print(selected_array)
