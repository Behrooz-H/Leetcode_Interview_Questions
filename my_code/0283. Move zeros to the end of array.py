"""
283. Move all zeros to the end of array
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left= right=0
        while right<len(nums):
            if nums[right]!=0:
                nums[right], nums[left]= nums[left], nums[right]
                left+=1
            right+=1
            
            
"""TIme = O(N)
 Space= O(1)
"""


