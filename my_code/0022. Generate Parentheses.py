"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""

# in BRUTE FORCE We generate O (2^2*n) distinct states and check how many are valid


# Backtracking
# Time Complexity : O(4^N / N^ (1/2))
from typing import List


class Solution:
    @staticmethod
    def generateParenthesis(n: int) -> List[str]:
        ans = []

        def backtrack(S=None, left=0, right=0):
            S = [] if not S else S
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right + 1)
                S.pop()

        backtrack()
        return ans


if __name__=="__main__":
    sol = Solution()
    sol.generateParenthesis(4)



# Time Complexity O(n^4/n^(1/2))
# Space Complexity =O(N)