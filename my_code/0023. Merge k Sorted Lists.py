"""
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
"""

#divide and conquer - Merge two  sublist and then merge the merged results until no further sublist exists

from typing import Optional,List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2): # merge them two by two like a two linkedlist merge problem
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next

        if not l1:
            point.next = l2
        else:
            point.next = l1

        return head.next

"""
Time complexity : O(Nlogk) where k is the number of linked lists.
We can merge two sorted linked list in O(n) time where n is the total number of nodes in two lists.
Sum up the merge process and we can get:O(Nlogk)

Space complexity : O(1)
We can merge two sorted linked lists in O(1) space.
"""



class Solution_for_array_list:
    @staticmethod
    def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """

        :type lists: object
        """
        def merge_two_list(l1:list, l2:list)->list:
            res=[]
            while l1 and l2:
                res.append(l1.pop(0) if l1[0]<l2[0] else l2.pop(0))
            res.extend(l1 if l1 else l2)
            return res
        while len(lists)>1:
            ans=[]
            for i in range(0,len(lists),2):
                ans.append(merge_two_list(lists[i], lists[i+1] if i+1<len(lists) else []))
            lists=ans
        return lists
