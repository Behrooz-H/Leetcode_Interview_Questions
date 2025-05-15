"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""



class Solution:
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next

"""
Time complexity : O(n+m)
Because exactly one of l1 and l2 is incremented on each loop
iteration, the while loop runs for a number of iterations equal to the
sum of the lengths of the two lists. All other work is constant, so the
overall complexity is linear.

Space complexity : O(1)
The iterative approach only allocates a few pointers, so it has a
constant overall memory footprint.
"""



# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return
        if not l2 and l1:
            return l1
        if not l1 and l2:
            return l2
        if l1.val<=l2.val:
            head, current= l1, l1
            l1= l1.next
        else:
            head, current= l2, l2
            l2= l2.next
        while l1 and l2 :
            if l1.val<=l2.val:
                current.next=l1
                current=l1
                l1=l1.next
            if current and l2 and l1 and l2.val<=l1.val:
                current.next=l2
                current= l2
                l2=l2.next
        current.next = l1 if l1 else l2
        return head

