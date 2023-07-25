"""
Merge sort algorithm implementation.
Time complexity: best, worst, average = O(n log n)
Space complexity: O(n)

How it works:
1. Divide the array in half, until each sub-array contains a single element.
2. Sort each half.
3. Merge the two halves, by comparing each element in each half, and placing the smaller element first.

Merge steps is the most important part of this algorithm.
    How to combine parts with 1 element. Easy. But how to combine parts with 2 or more elements?
    1. Create a new array, with the size of the sum of the sizes of the two arrays.
    2. The algorithm maintains three pointers, one for each of the two arrays and one for maintaining the current index of the final sorted array.

Here is the merge step algorithm:
    Have we reached the end of any of the arrays?
    No:
        Compare current elements of both arrays
        Copy smaller element into sorted array
        Move pointer of element containing smaller element
    Yes:
        Copy all remaining elements of non-empty array
"""


def merge_sort(array):
    if len(array) > 1:

        # r is the point where the array is divided into two subarrays
        r = len(array) // 2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        merge_sort(L)
        merge_sort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


if __name__ == '__main__':
    unsorted_array = [6, 5, 12, 10, 9, 1]
    merge_sort(unsorted_array)
    print(unsorted_array)
