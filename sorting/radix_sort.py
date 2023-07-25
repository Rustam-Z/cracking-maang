"""
Radix sort algorithm.

Algorithm:
    1. Find the max element in the array to find the number of digits. And use this to find number of loops.
    2. Now, go through each digit, starting from the end. And sort the array based on the digit. Use any stable sort.
       Stable sorting preserves the order for the same elements.
    3. Repeat step 2 for all digits.

Time complexity: O(nk), where n is the number of elements, and k is the number of digits in the largest element.
Space complexity: O(n+k)x`
"""


def sort(array, place) -> list:
    """
    This is any stable sort algorithm, that sorts the array based on the order of digit.
    Usually counting sort is used, because the range of numbers are between [0...9].
    Example: [111, 222, 112, 333], place = 2, that means we need to sort based on second digit.
    """
    ...


def radix_sort(array) -> list:
    # Step 1 -> Find the maximum element in the input array
    max_element = max(array)

    # Step 2 -> Find the number of digits in the `max` element
    number_of_digits = 1
    while max_element > 0:
        max_element /= 10
        number_of_digits += 1

    # Step 3 -> Initialize the place value to the least significant place
    place = 1

    # Step 4
    output_array = array
    while number_of_digits > 0:
        output_array = sort(output_array, place)
        place *= 10  # 1, 10, 100, 1000, ...
        number_of_digits -= 1

    return output_array


if __name__ == '__main__':
    unsorted_array = [121, 432, 564, 23, 1, 45, 788]
    radix_sort(unsorted_array)
    print(unsorted_array)
