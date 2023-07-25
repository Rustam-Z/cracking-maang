"""
Insertion sort algorithm implementation.

Algorithm:
    1. Iterate from arr[1] to arr[n] over the array.
    2. Compare the current element (key) to its predecessor.
    3. If the key element is smaller than its predecessor, compare it to the elements before.
        Move the greater elements one position up to make space for the swapped element.

Advantages:
    1. Works with floating point numbers.
    2, Works with negative numbers.
    3. Works with duplicate elements.
    4. Good for small data sets.

Time complexity:
    Best O(n)
    Worst O(n^2)
    Average O(n^2)
Space complexity: O(1)
"""


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # for descending order, change key < array[j] to key > array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        # Place key after the element that is just smaller than it.
        array[j + 1] = key
    return array


if __name__ == '__main__':
    unsorted_array = [5, 2, 4, 6, 1, 3, 1.2, 2, 2, -10]
    sorted_array = insertion_sort(unsorted_array)
    print(sorted_array)
