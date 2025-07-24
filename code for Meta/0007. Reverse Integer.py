"""
7. Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""

# Time Complexity: O(log(x). There are roughly \log_{10}(x) digits in xx.
# Space Complexity: O(1).


class Solution:
    def reverse(self, x:int) :
        rev = 0
        flag = -1 if x<0 else 1
        x=x*flag
        while x != 0:
            pop = x % 10
            x //= 10
            rev = rev * 10 + pop
            if flag * rev > (2**31)-1 or flag * rev < -2**31:  # or (rev == Integer.MAX_VALUE / 10 and pop > 7)
                return 0
        return flag * rev



class Week_solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        val=int(x[::-1] if x[0]!="-" else '-'+x[:0:-1])
        return  val if -2**31<val<2**31-1 else 0


if __name__=="__main__":
    sol=Solution()
    sol.reverse(-321)
