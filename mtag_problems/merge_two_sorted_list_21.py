
'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            firstPointer = lastPointer = list1
            list1 = list1.next
        else:
            firstPointer = lastPointer = list2
            list2 = list2.next

        while list1 and list2:
            if list1.val <= list2.val:
                lastPointer.next = list1
                list1 = list1.next
            else:
                lastPointer.next = list2
                list2 = list2.next
            lastPointer = lastPointer.next
        if list1:
            lastPointer.next = list1
        if list2:
            lastPointer.next = list2
        return firstPointer
