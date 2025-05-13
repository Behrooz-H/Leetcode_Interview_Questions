"""
Given the head of a singly linked list and two integers left and right where left <= right,
 reverse the nodes of the list from position left to position right, and return the reversed list.

"""


# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head, left, right):
        curr_node = head
        next_node = curr_node.next
        while left < right and next_node:
            tmp = next_node.next
            next_node.next = curr_node
            curr_node = next_node
            next_node = tmp
            left += 1
        return head, curr_node, next_node

    def reverseBetween(self, head: [ListNode], left: int, right: int) -> [ListNode]:
        if left == right:
            return head
        start = 1
        start_node = head
        prev_start = None
        while start < left and start:
            prev_start = start_node
            start_node = start_node.next
            start += 1
        tail, header, tail_next = self.reverse(start_node, left, right)
        if prev_start:
            prev_start.next = header
        else:
            head = header
        tail.next = tail_next
        return head

def printer(head):
    lst = ""
    while head:
        if head.next:
            lst+=str(head.val)+"--->"
        else:
            lst+=str(head.val)
        head=head.next
    print(lst)


if __name__ == '__main__':
    a= ListNode(1)
    b= ListNode(2)
    c= ListNode(3)
    d= ListNode(4)
    e= ListNode(5)
    f= ListNode(6)
    g= ListNode(7)
    h= ListNode(8)
    a.next =b
    b.next = c
    c.next = d
    d.next = e
    e.next =f
    f.next = g
    g.next = h
    ls = Solution()
    printer(a)
    a=ls.reverseBetween(a , 1 ,8)
    printer(a)
