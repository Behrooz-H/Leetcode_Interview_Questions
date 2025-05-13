"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
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
