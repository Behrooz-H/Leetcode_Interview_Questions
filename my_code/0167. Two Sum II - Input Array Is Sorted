"""
167. Two Sum II - Input Array Is Sorted
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

"""

from typing import List


# Time Complexity = O(N) and Space Complexity = O(1)

class Solution1:
    def twoSum(self, numbers:List[int],target:int):
        low ,high =0, len(numbers) - 1
        while low < high:
            sum = numbers[low] + numbers[high]
            if sum == target:
                return low + 1, high + 1
            if sum < target:
                low+=1
            else:
                high-=1
        return {-1, -1}



from typing import List
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            r,l = (r-1, l)if numbers[l]+numbers[r]>target else (r,l+1)
        return [-1,-1]
