"""
560. Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
"""



    
"""
Time complexity : O(n). The entire nums array is traversed only once.
Space complexity : O(1). Hashmap map can contain up to n distinct entries in the worst case.
"""



# The idea behind this approach is as follows: 
#     If the cumulative sum(represented by sum[i] for sum up to i th
#   index) up to two indices is the same, the sum of the elements lying in between those indices is zero. 
# Extending the same thought further, if the cumulative sum up to two indices, say i and j is at a difference of k i.e.
# if sum[i]−sum[j]=k, the sum of elements lying between indices i and j is k.            
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count =  sum_ = 0
        map_ = {0: 1}
        
        for num in nums:
            sum_ += num
            if sum_ - k in map_:
                count += map_[sum_ - k]
            map_[sum_] = map_.get(sum_, 0) + 1
            
        return count
    
    
    
    
    
    
    
#O(n^2)    # If it is only positive integerss in the Array
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        left=right=0
        res=[]
        while right<len(nums):
            checksum = sum(nums[left:right+1])
            if checksum == k:
                res.append([left, right])
            if checksum > k:
                left+=1
                if right<left:
                    right=left
            else:
                right+=1
        return len(res)