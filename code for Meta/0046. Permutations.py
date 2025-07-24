"""
46. Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

--------------------

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

"""



from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        def backtrack(done:int=0):
            if done==n:
                res.append(nums[:])
            else:
                for i in range(done, n):
                    # place i-th integer first
                    # in the current permutation
                    nums[done], nums[i] = nums[i], nums[done]
                    # use next integers to complete the permutations
                    backtrack(done + 1)
                    # backtrack
                    nums[done], nums[i] = nums[i], nums[done]
        backtrack()
        return res


"""
Time complexity, what you should say in an interview: O(n⋅n!)
Finding permutations is a well-studied problem in combinatorics. Given a set of length n, the number of permutations is n! (n factorial). There are n options for the first number, n−1 for the second, and so on.

For each of the n! permutations, we need O(n) work to copy curr into the answer. This gives us O(n⋅n!) work."""

if __name__=="__main__":
    sol=Solution()
    print(sol.permute([1,2,3,4]))
