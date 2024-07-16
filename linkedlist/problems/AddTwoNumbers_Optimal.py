# Definition for singly-linked list.
from typing import Optional

##n optimul solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        carry = 0

        while l1 or l2 or carry != 0:
            sum_value = carry
            if l1:
                sum_value += l1.val
                l1 = l1.next
            if l2:
                sum_value += l2.val
                l2 = l2.next
            carry = sum_value // 10
            current.next = ListNode(sum_value % 10)
            current = current.next
        return dummy.next


# Example usage
# Creating linked lists representing the numbers 942 and 9465 (in reverse)
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(9)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(9)

solution = Solution()
result = solution.addTwoNumbers(l1, l2)
# Print the result linked list
current = result
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")  # Output: 9 -> 7 -> 5 -> None

# Creating linked lists representing the numbers 9999999 and 9999 (in reverse)
l3 = ListNode(9)
l3.next = ListNode(9)
l3.next.next = ListNode(9)
l3.next.next.next = ListNode(9)
l3.next.next.next.next = ListNode(9)
l3.next.next.next.next.next = ListNode(9)
l3.next.next.next.next.next.next = ListNode(9)

l4 = ListNode(9)
l4.next = ListNode(9)
l4.next.next = ListNode(9)
l4.next.next.next = ListNode(9)

solution1 = Solution()
result1 = solution1.addTwoNumbers(l3, l4)
# Print the result linked list
current1 = result1
while current1:
    print(current1.val, end=" -> ")
    current1 = current1.next
print("None")  # Output: 9 -> 7 -> 5 -> None