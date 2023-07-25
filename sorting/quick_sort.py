"""
Quick sort algorithm implementation.

Algorithm:
    1. Select a pivot, normally (random, first, last, or middle) element.
    2. Compare the pivot with each element in the array, elements smaller than pivot are placed at left and greater than pivot are placed at right.
    3. Repeat step 2 recursively until all elements are sorted.

    Second step is very important, it is called partitioning.
    1. We select pivot as last element.
    2. Left pointer will point to first element.
    3. If element smaller than pivot is found, we swap it with element at left ptr. And left ptr will be incremented by 1.
    4. If element greater than pivot is found, we do nothing.
    5. After all the iterations, we swap pivot with element at greater pointer.


Time complexity:
    Best case: O(n log n)
    Average case: O(n log n)
    Worst case: O(n^2)
Space complexity: O(log n), because recursive stack can max uses half of array
"""


# function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            array[i], array[j] = array[j], array[i]

    # swap the pivot element with the greater element specified by i
    array[i + 1], array[high] = array[high], array[i + 1]

    # return the position from where partition is done
    return i + 1


# function to perform quicksort
def quick_sort(array, low, high):
    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # recursive call on the left of pivot
        quick_sort(array, low, pi - 1)

        # recursive call on the right of pivot
        quick_sort(array, pi + 1, high)


if __name__ == '__main__':
    unsorted_array = [-5, 10, 7, 8, 9, 1, 5, -2]
    quick_sort(unsorted_array, 0, len(unsorted_array) - 1)
    print(unsorted_array)
