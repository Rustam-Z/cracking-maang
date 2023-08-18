# Linked List

[Linked list Python implementation](linked_list.py)

### Need to know
1. Use `while` loop while working with linked list
2. Get node value at some index
3. Add node at head, add at tail, add at index
4. Delete node at head, delete at tail, delete at index
5. The "Runner" technique = fast and slow pointers
6. Recursion
7. Reverse the linked list


```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
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
```