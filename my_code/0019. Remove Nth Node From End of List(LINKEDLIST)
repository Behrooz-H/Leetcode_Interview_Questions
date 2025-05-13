"""
19. Remove Nth Node From End of List (LINKEDLIST)
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""


# Definition for singly-linked list.
# from typing import Optional
# Time complexity : O(L)
# The algorithm makes one traversal of the list of L nodes. Therefore time complexity is O(L)
#
# Space complexity : O(1)
# We only used constant extra space.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def removeNthFromEnd(head: ListNode, n: int):
        dummy = ListNode(0, head)
        first, second = dummy, dummy
        # Advances first pointer so that the gap between  first and second is n  nodes   apart
        for _ in range(n + 1):
            first = first.next
        # Move first to the end, maintaining the gap
        while first:
            first, second = first.next, second.next
        second.next = second.next.next
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    sol.removeNthFromEnd(ListNode(1), 1)
