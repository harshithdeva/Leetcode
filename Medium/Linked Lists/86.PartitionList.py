#Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        prev1 = dummy1
        prev2 = dummy2
        temp = head
        while temp:
            if temp.val < x:
                prev1.next = temp
                prev1 = temp
            else:
                prev2.next = temp
                prev2 = temp
            temp = temp.next
        prev1.next = dummy2.next
        prev2.next = None
        head = dummy1.next

        return head
        