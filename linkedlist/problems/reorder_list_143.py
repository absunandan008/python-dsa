# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #First we find the middle of list
        #We reverse the second half
        #we merge both half

        #Find Middle of list
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #now slow is middle of list
        #so we reverse the second half
        curr, prev =  slow, None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        #now we have reverse the second half, now we just need to merge two list
        first, second = head, prev
        while second.next:
            tmp = first.next
            first.next = second
            first = tmp

            tmp = second.next
            second.next = first
            second = tmp