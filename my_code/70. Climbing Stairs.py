"""
70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


 # It is like fibbonacci but with start from 1,2 and add 1,2 --> give 3 and add 3+2--> give 5

# Both Top down and Bottom up


#  Time complexity : O(n). Single loop up to n.
# Space complexity : O(n). dp array of size n is used.
class Dynamic_programmming_Solution:
    @staticmethod
    def climbStairs(n):
        if n <= 1:
            return n
        dp =[1,2]
        for i in range(2,n):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]



# Bad Solution  Time:O(2^N) with memoization it becomes  O(N)
class BadSolution:
    def climbStairs(self, n):
        def climb_Stairs(i, n):
            if i > n:
                return 0
            if i == n:
                return 1
            return climb_Stairs(i + 1, n) + climb_Stairs(i + 2, n)
        return climb_Stairs(0, n)
