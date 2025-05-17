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



class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N==0:
            return []
        if N == 1:
            return [i for i in range(10)]

        # initialize the queue with candidates for the first level
        queue = [digit for digit in range(1, 10)]

        for level in range(N-1):
            next_queue = []
            for num in queue:
                tail_digit = num % 10
                # using set() to avoid duplicates when K == 0
                next_digits = set([tail_digit + K, tail_digit - K])

                for next_digit in next_digits:
                    if 0 <= next_digit < 10:
                        new_num = num * 10 + next_digit
                        next_queue.append(new_num)
            # start the next level
            queue = next_queue

        return queue

"""_summary_
Time Complexity: O(2**N)
Essentially with the BFS approach, all the intermeidate candidates form a binary tree, same as the execution tree as in the DFS approach.
Only this time, we traverse in a breadth-first manner, rather than the depth-first.
Therefore, the overall time complexity of the algorithm would be O(2^N).

Space Complexity: O(2^N) or (2**N)
We use two queues to maintain the intermediate solutions, which contain no more than two levels of elements.
The number of elements at the level of i is up to 9⋅2 
i−1
 .

To sum up, the space complexity of the algorithm would be O(9⋅2 
N−1
 +9⋅2 
N−2
 )=O(2 
N
 ).
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