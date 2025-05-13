"""
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""
# Approach: Binary Search O(logN)

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        lower_bound = self.findBound(nums, target, True)
        if (lower_bound == -1):
            return [-1, -1]

        upper_bound = self.findBound(nums, target, False)

        return [lower_bound, upper_bound]

    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        begin, end = 0, len(nums) - 1
        while begin <= end:
            mid = int((begin + end) / 2)
            if nums[mid] == target:
                if isFirst:
                    # This means we found our lower bound.
                    if mid == begin or nums[mid - 1] < target:
                        return mid
                    # Search on the left side for the bound.
                    end = mid - 1
                else:
                    # This means we found our upper bound.
                    if mid == end or nums[mid + 1] > target:
                        return mid
                    # Search on the right side for the bound.
                    begin = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
        return -1

"""
Time Complexity= O(Log n)
Space Complexity= O(1)
"""


class Solution2:

    def search (self,l,r, nums, target):
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                return mid
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        first_position= self.search(0, len(nums)-1, nums , target)
        if first_position==-1:
            return [-1,-1]
        tmp_f, first , last, tmp_l =first_position, first_position, first_position, first_position,
        while first!=-1:
            tmp_f=first
            first=self.search(0, first-1, nums, target)
        while last!=-1:
            tmp_l=last
            last=self.search(last+1,len(nums)-1, nums, target)
        return [tmp_f, tmp_l]


if __name__=="__main__":
    a=Solution()
    print(a.searchRange([1,2,3,4,5,6,7,8,8,8,8,8,8,8,8,9,10],8))

# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:

#         if nums.count(target) < 1:
#             return [-1, -1]
#         else:
#             return [nums.index(target), len(nums) - nums[::-1].index(target) - 1]
