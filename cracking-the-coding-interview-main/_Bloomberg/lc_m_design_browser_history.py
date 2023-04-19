"""1472. Design Browser History
https://leetcode.com/problems/design-browser-history/

Problem: Implement visit(url), back(steps), forward(steps) for saving browser history.
    visit(url: str) -> None
    back(steps: int) -> url: str
    forward(steps: int) -> url: str

Constraints:
    - visit() clears forward history
    - If you can only return x steps in the history and steps > x, you will return only x steps.

Solution 1: Array + deletion
    - Use array/stack and pointer, array is for saving the urls, and pointer is to understand where the user is now.
    - Visit O(N) because of delete, but back and forward are O(1) time complexity

Solution 2: Doubly Linked List
    - Visit O(1), back and visit are O(steps)

Solution 3: Array + overwriting items
    - All operations are O(1) time
"""


"""
Solution 1: Array + pointer
"""


class BrowserHistoryArray:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_page_pointer = 0

    # Time O(n) - Apparently del is O(n)
    def visit(self, url: str) -> None:
        # Removing forward history, if we are not in last page.
        if self.current_page_pointer < len(self.history) - 1:
            del self.history[self.current_page_pointer + 1:]

        self.history.append(url)
        self.current_page_pointer += 1

    # Time O(1)
    def back(self, steps: int) -> str:
        first_page = 0
        number_of_pages_back = self.current_page_pointer - steps
        self.current_page_pointer = max(first_page, number_of_pages_back)
        return self.history[self.current_page_pointer]

    # Time O(1)
    def forward(self, steps: int) -> str:
        last_page = len(self.history) - 1
        number_of_pages_forward = self.current_page_pointer + steps
        self.current_page_pointer = min(last_page, number_of_pages_forward)
        return self.history[self.current_page_pointer]


"""
Solution 2: Double linked list
"""


class ListNode:
    def __init__(self, val="", next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistoryLinkedList:
    # Space O(number_of_pages_visited)
    def __init__(self, homepage: str):
        self.current_page = ListNode(val=homepage)

    # Time O(1)
    def visit(self, url: str) -> None:
        self.current_page.next = ListNode(val=url, prev=self.current_page)
        self.current_page = self.current_page.next

    # Time O(steps)
    def back(self, steps: int) -> str:
        while self.current_page.prev and steps > 0:
            steps -= 1
            self.current_page = self.current_page.prev
        return self.current_page.val

    # Time O(steps)
    def forward(self, steps: int) -> str:
        while self.current_page.next and steps > 0:
            steps -= 1
            self.current_page = self.current_page.next
        return self.current_page.val


"""
Solution 3: Array solution + pointer + we won't remove items but we will overwrite instead.
"""


class BrowserHistoryArrayWithoutDeletion:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_page_pointer = 0
        self.current_boundary = 0

    # Time O(1)
    def visit(self, url: str) -> None:
        if self.current_page_pointer == len(self.history) - 1:
            self.history.append(url)
        else:
            self.history[self.current_page_pointer + 1] = url

        self.current_page_pointer += 1
        self.current_boundary = self.current_page_pointer

    # Time O(1)
    def back(self, steps: int) -> str:
        first_page = 0
        number_of_pages_back = self.current_page_pointer - steps
        self.current_page_pointer = max(first_page, number_of_pages_back)
        return self.history[self.current_page_pointer]

    # Time O(1)
    def forward(self, steps: int) -> str:
        last_page = self.current_boundary
        number_of_pages_forward = self.current_page_pointer + steps
        self.current_page_pointer = min(last_page, number_of_pages_forward)
        return self.history[self.current_page_pointer]
