"""
21. Merge Two Sorted Lists: https://leetcode.com/problems/merge-two-sorted-lists/

Problem: Merge Two Sorted Lists

Input: Two heads of linked lists
Output: Merged list

SOLUTION 1:
    - Convert the LL to array
    - Combine both arrays
    - Sort the resultant array
    - Create another LL
    - Time comp: O(nlogn) where n is len of longer LL
    - Space comp: O(n)
SOLUTION 2:
    - Iterate over both lists at the same time
    - Create a dummy node, and insert one by one
    - After loop finish, insert the tail that left
    - Time: O(n)
    - Space: O(1)
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def brute_force(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Algorithm:
        - Create arrays from both lists, merge two arrays, sort array.
        - Create another linked list, and create nodes.

    Time comp: O(nlogn) where n is len of longer LL
    Space comp: O(n)
    """

    def create_array_from_list(head: Optional[ListNode]) -> list:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return nums

    def create_list_from_array(nums: list) -> Optional[ListNode]:
        if not nums:
            return None

        head = ListNode(nums[0])
        curr = head
        for num in nums[1:]:
            curr.next = ListNode(num)
            curr = curr.next

        return head

    nums1 = create_array_from_list(list1)
    nums2 = create_array_from_list(list2)

    combined_nums = sorted(nums1 + nums2)

    return create_list_from_array(combined_nums)


def optimal_solution(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Algorithm:
        - Create new linked list
        - Traverse over both linked lists, compare values, add node to new LL.

    Time complexity: O(n)
    Space complexity: O(1)
    """

    # Edge cases
    if not list1:
        return list2

    if not list2:
        return list1

    dummy = ListNode()
    curr = dummy

    while list1 and list2:  # We traverse until the smallest length list.
        if list1.val >= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next

        curr = curr.next

    if list1:
        curr.next = list1
    elif list2:
        curr.next = list2

    return dummy.next


def merge_k_sorted_lists(lists):
    """
    https://leetcode.com/problems/merge-k-sorted-lists/
    """
    # Edge cases
    if not lists:
        return None

    if len(lists) == 1:
        return lists[0]

    def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Algorithm:
            - Create new linked list
            - Traverse over both linked lists, compare values, add node to new LL.

        Time complexity: O(n)
        Space complexity: O(1)
        """

        # Edge cases
        if not list1:
            return list2

        if not list2:
            return list1

        dummy = ListNode()
        curr = dummy

        while list1 and list2:  # We traverse until the smallest length list.
            if list1.val >= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return dummy.next

    while len(lists) > 1:
        list1 = lists.pop()
        list2 = lists.pop()
        merged_list = merge_two_lists(list1, list2)
        lists.append(merged_list)

    return lists[0]
