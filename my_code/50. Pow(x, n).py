"""
50. Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^(-2) = (1/2) ^2 = 1/4 = 0.25
"""

# Time O(LOG N)
# SPACE = O(1)
class Solution:
    def myPow(self,x:float, n:int):
        if n==0:
            return 1
        if n < 0:
            x = 1 / x
            n = -1*n
        ans ,current_product  , i = 1, x, n
        while i>0:
            if i % 2 == 1:
                ans *=  current_product
            i//=2
            current_product = current_product * current_product
        return ans





# Time O(LOG N)
# SPACE = O(LOG N)
class Second_Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            x,n = 1/x , -n
        def fast_pow(x, n):
            if n==1:
                return x
            if n==0:
                return 1
            half= fast_pow(x,n//2)
            if n % 2==0:
                return half*half
            else:
                return half*half*x
        return fast_pow(x,n)




# Time O(N)
# Space O(1)
class Brute_force_Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            n, x =-1*n, 1/x
        ans=1
        for i in range(n):
            ans*=x
        return ans


if __name__=="__main__":
    ssol=Second_Solution()
    sol= Solution()
    # print(ssol.myPow(3,5))
    print(sol.myPow(3, 5))
