"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self, head:ListNode, next=None):
        self.head=head
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummyHead = ListNode(0)
        cur = dummyHead
        while l1 or l2 or carry:
            l1_val= l1.val if l1 else 0
            l2_val= l2.val if l2 else 0
            cur.val=(l1_val+l2_val+carry)%10
            carry=(l1_val+l2_val+carry)//10
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            if l1 or l2 or carry:
                new=ListNode()
                cur.next=new
                cur=new
        return dummyHead

if __name__== "__main__":
    temp= ListNode()
    ll1 = LinkedList(head=l1)
    for i in range(2,8,3):
        temp.val= i
        new=ListNode()
        l1.next=new
        l1=new
    l2= ListNode(5)
    ll2=LinkedList(head=l2)
    for i in range(3,10,2):
        l2.val= i
        new=ListNode()
        l2.next=new
        l2=new
    for i in [ll1,ll2]:
        l=i.head
        while l :
            print(l.val)