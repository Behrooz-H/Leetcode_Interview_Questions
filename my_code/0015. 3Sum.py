"""
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
 i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

"""

from typing import List
# O(N^2) two fr loops  No sort needed
# O

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res,  seen = set(),   {}
        for i, val1 in enumerate(nums):
            # if val1 not in dups:
            #     dups.add(val1)
                for  val2 in nums[i+1:]:
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i: # if ithas been seen in the round for this round
                        res.add(sorted((val1, val2, complement)))
                    seen[val2] = i
        return list(res)

"""
Complexity Analysis

Time Complexity: O(n^2). We have outer and inner loops, each going through n elements.
While the asymptotic complexity is the same, this algorithm is noticeably slower than the previous approach. 
Lookups in a hashset, though requiring a constant time, are expensive compared to the direct memory access.
Space Complexity: O(n) for the hashset/hashmap.
For the purpose of complexity analysis, we ignore the memory required for the output. However, in this approach we also store output in the hashset for deduplication. 
In the worst case, there could be O(n^2) triplets in the output, 
like for this example: [-k, -k + 1, ..., -1, 0, 1, ... k - 1, k]. Adding a new number to this sequence will produce n / 3 new triplets.

"""

# needing sort
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1



