'''
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor
and successor pointers in a doubly-linked list. For a circular doubly linked list,
the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to
its predecessor, and the right pointer should point to its successor.
You should return the pointer to the smallest element of the linked list.
'''
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        self.first, self.last = None, None
        def dfs(node):
            if node:
                # normal DFS
                dfs(node.left)

                #in order traversel. If we do not see last node
                # then populate first node and then set it to last node
                if self.last:
                    self.last.right = node
                    node.left = self.last
                else:
                    self.first = node
                self.last = node
                #normal DFS
                dfs(node.right)
        dfs(root)

        # Make the linked list circular
        self.first.left = self.last
        self.last.right = self.first
        return self.first
    def treeToDoublyListSimple(self, root: 'Optional[Node]') -> 'Optional[Node]':
        ##Basically InOrder Traversal and then create a double linkedList
        if root is None:
            return None
        nums = []
        def dfs(node):
            if node is None:
                return None

            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)

        dfs(root)
        head =  Node(nums[0])
        prev = head
        for num in nums[1:]:
            newNode = Node(num)
            prev.right = newNode
            newNode.left = prev
            prev = newNode

        head.left = prev
        prev.right = head

        return head