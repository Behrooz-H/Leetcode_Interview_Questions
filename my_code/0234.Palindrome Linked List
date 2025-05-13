"""

Given the head of a singly linked list, return true if it is a palindrome.
"""
#  Best Approach O(N) using fast ruuner
class Solution:
    def palind(self, l):
        if not l.head or not l.head.next:
            return False
        slow, fast = l.head , l.head
        l=[]
        while fast:
            l.append(slow)
            slow=slow.next if slow.next else slow
            fast=fast.next.next if fast.next and fast.next.next else None
        i=-1
        while slow:
            if l[i] != slow or i<(len(l)*-1):
                return False
            i-=1
            slow=slow.next
        return True



#  TODO: SECOND  good approach
class Solution2:

    def palind(self, l):
        if not l.head or not l.head.next:
            return False
        cur = l.head
        rev, norm = [], []
        while cur:
            norm.append(cur)
            rev.insert(0, cur)
            cur = cur.next
        left, right = 0, len(norm)
        while left < right and left < len(rev) and right >= 0:
            if norm[left] != rev[right]:
                return False
            else:
                right -= 1
                left += 1
        return True


#  TODO: Third  good approach
import math
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution3:
    def isPalindrome(self, head:[ListNode]) -> bool:
        cur=head
        l=[]
        while cur:
            l.append(cur.val)
            cur=cur.next
        return l[:(len(l)//2)] == l[math.ceil(len(l)/2):][::-1]

a=Solution()
l=[1,2,3,2,1]
k=[1,2,2,1]
j=[1,2,3,4,3,2]
