function removeMiddleNode(head) {
  let slow = head,
    fast = head

  while (fast.next !== null && fast.next.next !== null) {
    slow = slow.next
    fast = fast.next.next
  }
  if (s === null || s.next === null) {
    return false
  }
  slow.value = slow.next.value
  slow.next = slow.next.next
  return true
}