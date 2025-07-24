"""
67. Add Binary
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"
    """
    
    
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ar=a[::-1]
        br=b[::-1]
        # ibia =0
        carry= 0
        sum_=""
        while ar or br or carry:
            a0 = ar[0] if ar  else  0
            b0 = br[0] if br else 0
            sum_+=(str((carry + int(a0) + int(b0)) %2))
            carry = (carry + int(a0) + int(b0)) //2
            ar = ar[1:] if ar else ""
            br = br[1:] if br else ""
        return sum_[::-1]
    
"""
Time complexity: O(max(N,M)), where N and M are lengths of the input strings a and b.
Space complexity: O(max(N,M)) to keep the answer.
"""
    
# Bit Manipulation
class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2) #convert a and b into the base 2 numbers
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]
    
    