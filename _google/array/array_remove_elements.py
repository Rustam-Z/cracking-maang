from typing import Optional


def remove_element_inplace(array: list, value: int) -> list:
    """
    https://leetcode.com/problems/remove-element/

    Problem: Given array, remove elements equal to "value" in-place.
    """
    def solution1(array: list, value: int) -> list:
        # SOLUTION 1: Use remove() method. Time complexity: O(n^2), Space complexity: O(1)

        i = 0
        while i < len(array):
            if array[i] == value:
                array.remove(array[i])
            else:
                i += 1

        return array

    def solution2(array: list, value: int) -> list:
        # SOLUTION 2: Use two pointers. Use reassignment. Time complexity: O(n), Space complexity: O(1)

        i = 0
        j = 0
        while j < len(array):
            if array[j] != value:
                array[i] = array[j]
                i += 1
            j += 1

        return array[:i]


def remove_duplicates_from_sorted_array_inplace(array: list) -> list:
    """
    https://leetcode.com/problems/remove-duplicates-from-sorted-array/

    Problem: Given sorted array, remove duplicates in-place.
    """

    def solution1_brute_force(array: list) -> list:
        """
        Time complexity: O(n^2)
        Space complexity: O(1)
        """
        i = 0
        while i < len(array) - 1:
            if array[i] == array[i + 1]:
                array.remove(array[i])
            else:
                i += 1

        return array

    def solution2_two_pointers(array: list) -> list:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        i = 0
        for j in range(1, len(array)):
            if array[j] != array[i]:
                i += 1
                array[i] = array[j]

        return array[:i + 1]


def remove_duplicates_from_sorted_array_inplace_twice(array: list) -> list:
    """
    https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

    Problem: Given sorted array, each element can appear at most twice. Remove the duplicates in-place.
    """

    def solution1_brute_force(array: list) -> list:
        """
        Time complexity: O(n^2)
        Space complexity: O(1)
        """
        i = 0
        while i < len(array) - 2:
            if array[i] == array[i + 1] == array[i + 2]:
                array.remove(array[i])
            else:
                i += 1

        return array

    def optimzed_solution(array: list) -> list:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        i = 0
        for j in range(1, len(array)):
            if array[j] != array[i]:
                i += 1
                array[i] = array[j]
            elif array[j] == array[i] and i == 0:  # Because we start with i = 0
                i += 1
                array[i] = array[j]
            elif array[j] == array[i] and array[i] != array[i - 1]:
                i += 1
                array[i] = array[j]

        return array[:i + 1]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_duplicates_from_sorted_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    https://leetcode.com/problems/remove-duplicates-from-sorted-list/

    Problem: Given sorted linked list, remove duplicates in-place.
    """
    def brute_force(head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Algorithm:
            - Convert linked list to array
            - Remove duplicates from array
            - Convert array to linked list

        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not head:
            return None

        # Convert linked list to array.
        current = head
        array = []
        while current:
            array.append(current.val)
            current = current.next

        # Remove duplicates from array.
        array = list(set(array))

        # Convert array to linked list.
        new_head = ListNode(array[0])
        current = new_head
        for i in range(1, len(array)):
            current.next = ListNode(array[i])
            current = current.next

        return new_head

    def optimal_solution(head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not head:
            return None

        current = head
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


def remove_duplicate_letters_from_string(string: str) -> str:
    """
    https://leetcode.com/problems/remove-duplicate-letters/

    Problem: Given string, remove duplicate letters.
    """

    def brute_force(string: str) -> str:
        """
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        new_string = ""
        for char in string:
            if char not in new_string:
                new_string += char

        return new_string

    def optimal_solution(string: str) -> str:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        stack = []
        seen = set()
        last_occurence = {char: i for i, char in enumerate(string)}

        for i, char in enumerate(string):
            if char not in seen:
                while stack and char < stack[-1] and i < last_occurence[stack[-1]]:
                    seen.remove(stack.pop())
                stack.append(char)
                seen.add(char)

        return "".join(stack)
