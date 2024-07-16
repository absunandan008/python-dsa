# Definition for singly-linked list.
from typing import Optional

## Not an optimul solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getSum(self, l: Optional[ListNode]) -> int:
        decimalPoint = 1
        sum = 0
        if not l:
            return sum
        while l:
            sum = sum + (l.val * decimalPoint)
            decimalPoint *= 10
            l = l.next
        return sum

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        print("------start------")
        sum1 = self.getSum(l1)
        print("sum1", sum1)
        sum2 = self.getSum(l2)
        print("sum2", sum2)
        sum = sum1 + sum2
        print("sum", sum)
        print("------end------")

        if sum == 0:
            return ListNode(0)
        # Convert the total_sum to a linked list
        dummy = ListNode()
        current = dummy
        for digit in str(sum):
            current.next = ListNode(int(digit))
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

