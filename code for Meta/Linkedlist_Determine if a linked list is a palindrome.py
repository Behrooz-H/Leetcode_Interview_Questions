"""Determine if a linked list is a palindrome."""

def palind(l):
    if not l.head or not l.head.next:
        return False
    cur=l.head
    rev , norm=[] , []
    while cur:
        norm.append(cur)
        rev.insert(0 , cur)
        cur=cur.next
    left,right = 0, len(norm)
    while left<right and left<len(rev) and right>=0:
        if norm[left]!=rev[right]:
            return False
        else:
            right-=1
            left+=1
    return True
