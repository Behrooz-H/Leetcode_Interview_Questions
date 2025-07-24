""" 
9. Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindrome
        # Numbers ending in 0 are not palindrome unless the number is 0 itself
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x //= 10
        
        # For even digits: x == reverted
        # For odd digits: x == reverted // 10
        return x == reverted or x == reverted // 10


""" 
Time Complexity: O(log₁₀(n))
Because we divide the number by 10 each time, the number of iterations is proportional to the number of digits.


Space Complexity: O(1)
We only use a few integer variables for computation; no extra data structures are used.


"""