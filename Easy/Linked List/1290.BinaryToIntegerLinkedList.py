#Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        temp = head
        decimal = 0
        while temp:
            decimal = decimal * 2 + temp.val
            temp = temp.next
        return decimal