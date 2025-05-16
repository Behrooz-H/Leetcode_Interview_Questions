"""
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
# Divide and Conquer

from typing import List

# Dynamic Prog
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]
        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        return max_subarray

if __name__=="__main__":
    sol=Solution()
    print(sol.maxSubArray([1,2,3,4,-9,1,2,-3,8,9,10]))


"""
Time complexity: O(N), where N is the length of nums.
We iterate through every element of nums exactly once.

Space complexity: O(1)
No matter how long the input is, we are only ever using 2 variables: currentSubarray and maxSubarray.
"""


# TIME: O(N^2)  and SPACE: O(1)
class BRUTE_FORCE_Solution:
    @staticmethod
    def maxSubArray(nums: List[int]) -> int:
        max_subarray = float("-inf")
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)

        return max_subarray
