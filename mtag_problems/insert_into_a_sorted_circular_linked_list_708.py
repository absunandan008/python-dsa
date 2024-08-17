"""
Given a Circular Linked List node, which is sorted in non-descending order,
write a function to insert a value insertVal into the list such that it remains a sorted circular list.
The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value.
After the insertion, the circular list should remain sorted.

If the list is empty (i.e., the given node is null), you should create a new single circular list
and return the reference to that single node. Otherwise, you should return the originally given node.
"""
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        #When there is no element in List
        if not head:
            newNode = Node(insertVal)
            newNode.next = newNode
            return newNode

        prev = head
        curr = head.next

        toInsert = False

        while True:
            if prev.val <= insertVal <= curr.val:
                #We found a place to insert
                toInsert = True
            elif prev.val > curr.val:
                #means we reached end of list
                if insertVal >= prev.val or insertVal <= curr.val:
                    #we found a place to insert
                    toInsert = True

            #if we have found a place to insert
            if toInsert:
                prev.next = Node(insertVal,curr)
                return head

            #if we have not found place to insert
            prev = curr
            curr = curr.next

            #looks like we have done full loop and found nothing
            if prev == head:
                break

        # Case #3.
        # did not insert the node in the loop
        prev.next = Node(insertVal, curr)
        return head
