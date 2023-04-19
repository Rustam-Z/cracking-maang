class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.swap(head)

    def swap(self, head):
        curr = head

        if head and head.next:
            curr = head.next
            head.next = self.swap(head.next.next)
            curr.next = head

        return curr