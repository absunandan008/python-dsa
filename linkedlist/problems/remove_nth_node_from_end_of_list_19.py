# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head
        for i in range(n):
            first = first.next
        #since we have reached the end of , that means n is equal to length. so remove first node
        if first is None:
            return head.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head
