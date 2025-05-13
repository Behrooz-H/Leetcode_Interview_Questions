"""
967. Numbers With Same Consecutive Differences

Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

You may return the answer in any order.



Example 1:

Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
"""


from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n==0:
            return []
        if n == 1:
            return [i for i in range(10)]
        ans = []
        def DFS(N, num):
            # base case
            if N == 0:
                return ans.append(num)
            tail_digit = num % 10
            # using set() to avoid duplicates when K == 0
            next_digits = set([tail_digit + k, tail_digit - k])

            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    new_num = num * 10 + next_digit
                    DFS(N - 1, new_num)

        for num in range(1, 10):
            DFS(n - 1, num)

        return list(ans)

class Week_solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res=[]
        for i in range(10**(n-1), 10**n):
            m=n
            j=i
            flag=True
            while m>1:
                if(( i//(10**(m-1)) - (i%(10**(m-1))//(10**(m-2)))) != k
                   and     ( i//(10**(m-1)) - (i%(10**(m-1))//(10**(m-2)))) != (-1*k)):
                    flag=False
                    break
                i=i%(10**(m-1))
                m-=1
            if flag:
                res.append(j)
        return res

class Week_solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res=[]
        for i in range(1, 10):
            if i + k < 10 and n > 1:
                res.append((i * (10 ** (n - 1))) + (i + k) * (10 ** (n - 2)))
            if i - k >= 0 and n > 1:
                res.append((i * (10 ** (n - 1))) + (i - k) * (10 ** (n - 2)))
        if k==2:
            return res
        def build(num,n)->List:
            m=n
            ans=[]
            while m>1:

            return ans

        fin=[]
        while res:
            num = res.pop(0)
            fin.extend(build(num, n))
