# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return 
        else:
            previous = head
            dupes = {previous.val}
            print(dupes)
            
            while previous.next:
                if previous.next.val in dupes:
                    previous.next = previous.next.next
                else:
                    dupes.add(previous.next.val)
                    previous = previous.next
        
            return head

