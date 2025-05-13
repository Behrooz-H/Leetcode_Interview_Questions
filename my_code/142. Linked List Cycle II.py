"""

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) :
        cur=head
        runner=cur.next
        while runner and cur and cur!=runner.next:
            cur=cur.next
            runner=runner.next.next
        if not runner:
            return None
        else :
            return runner.next if runner.next else None
