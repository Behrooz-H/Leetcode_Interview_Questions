"""
41. First Missing Positive
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.



Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # Base case.
        if 1 not in nums:
            return 1

        # Replace negative numbers, zeros,
        # and numbers larger than n by 1s.
        # After this convertion nums will contain
        # only positive numbers.
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1

        # Use index as a hash key and number sign as a presence detector.
        # For example, if nums[1] is negative that means that number `1`
        # is present in the array.
        # If nums[2] is positive - number 2 is missing.
        for i in range(len(nums)):
            a = abs(nums[i])
            # If you meet number a in the array - change the sign of a-th element.
            # Be careful with duplicates : do it only once.
            if a == len(nums):
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])

        # Now the index of the first positive number
        # is equal to first missing positive.
        for i in range(1,len(nums)):
            if nums[i] > 0:
                return i

        if nums[0] > 0:
            return len(nums)

        return n + 1
