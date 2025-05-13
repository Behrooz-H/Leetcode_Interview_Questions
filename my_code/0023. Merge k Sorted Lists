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

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two_lists(l1, l2):
            # maintain an unchanging reference to node ahead of the return node.
            prehead= prev = ListNode(-1)
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

        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = merge_two_lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if lists else None









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
