from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        # Traverse both lists
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # Get current value or 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            # Move to next nodes if available
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy_head.next
    


#Alternate Brute Force Method

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Convert first list to number
        temp_list1 = []
        while l1:
            temp_list1.append(l1.val)
            l1 = l1.next
        temp_list1.reverse()

        # Convert second list to number
        temp_list2 = []
        while l2:
            temp_list2.append(l2.val)
            l2 = l2.next
        temp_list2.reverse()

        # Convert to integers, add, and then back to list of digits
        sum_of_lists = int("".join(map(str, temp_list1))) + int("".join(map(str, temp_list2)))
        final_digits = list(map(int, str(sum_of_lists)[::-1]))
        
        # Build resulting linked list
        dummy = ListNode(0)
        current = dummy
        for digit in final_digits:
            current.next = ListNode(digit)
            current = current.next

        return dummy.next
