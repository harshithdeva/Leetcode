from typing import Optional
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
           return None
        current = head
        while current:
            runner = current
            while runner.next:
                if runner.next.val == current.val:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

        return head