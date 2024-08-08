
'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            current_copy = current.next
            current.next = prev
            prev = current
            current = current_copy
        return prev

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        p = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return p

