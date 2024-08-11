from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        # Creating a new weaved list of original and copied nodes.
        ptr = head

        # Inserting the cloned node just next to the original node.
        # If A->B->C is the original linked list,
        # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
        while ptr:
            new_node = Node(ptr.val, None, None)
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next
        ptr = head

        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old = head
        ptr_new = head.next # A->B->C
        head_new = head.next # A'->B'->C'

        while ptr_old:
            ptr_old.next = ptr_old.next.next
            ptr_new.next = ptr_new.next.next if ptr_new.next else None
            ptr_old = ptr_old.next
            ptr_new = ptr_new.next
        return head_new

    def copyRandomListIterative(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_dict = {}

        def clone_node(node):
            if node is not None:
                if node in node_dict:
                    return node_dict[node]
                else:
                    newNode = Node(node.val, None, None)
                    node_dict[node] = newNode
                    return newNode
            return None
        #######
        if head is None:
            return None
        old_node = head
        new_node = Node(old_node.val, None, None)
        node_dict[old_node] = new_node
        while old_node is not None:
            new_node.random = clone_node(old_node.random)
            new_node.next = clone_node(old_node.next)
            old_node = old_node.next
            new_node = new_node.next

        return node_dict[head]
