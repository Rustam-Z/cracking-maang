def reverseList(head):
    prev, curr = None, head

    while curr:
        tmp = curr.next
        
        curr.next = prev
        prev = curr
        curr = tmp
    
    return prev
    