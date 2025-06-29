# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        left -= 1
        right -= 1

        for _ in range(left):
            prev = prev.next
        current = prev.next

        loop_time= right-left
        for _ in range(loop_time):
            to_move = current.next
            current.next = to_move.next
            to_move.next = prev.next
            prev.next = to_move
        
        head = dummy.next

        return head