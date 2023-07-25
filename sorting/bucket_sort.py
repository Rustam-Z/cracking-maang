"""
Bucket sort.

Algorithm:
    1. Create n empty buckets.
    2. Insert items into their respective buckets.
    3. Sort the items in each bucket.
    4. Concatenate the sorted buckets.

Time complexity: O(n + k), where n is the number of elements, and k is the number of buckets.
Space complexity: O(n + k)
"""


def bucket_sort_for_float_nums(array):
    bucket = []

    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in array:
        index_b = int(10 * j)  # Because input is float.
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements by concatenating all buckets.
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


if __name__ == "__main__":
    unsorted_array = [.42, .32, .33, .52, .37, .47, .51]
    print("Sorted Array in descending order is")
    print(bucket_sort_for_float_nums(unsorted_array))
