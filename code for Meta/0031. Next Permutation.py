"""
31. Next Permutation
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.
"""

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i],nums[j] = nums[j], nums[i]
        # self.reverse(nums, i + 1)
        return nums[:i+1]+ list(reversed(nums[i+1:]))
    # def reverse(self, nums, start):
    #     i, j = start, len(nums) - 1
    #     while i < j:
    #         self.swap(nums, i, j)
    #         i += 1
    #         j -= 1

    # def swap(self, nums, i, j):
    #     temp = nums[i]
    #     nums[i] = nums[j]
    #     nums[j] = temp
        

""" 
Time complexity: O(n)

The first while loop runs at most n iterations, decrementing the variable i as it searches for the first decreasing element from the right. In the worst case, it checks all elements, so it takes O(n) time.

The second while loop also runs at most n iterations, decrementing the variable j as it searches for the smallest element larger than nums[i]. Similarly, it can take O(n) time.

The reverse function is called on a portion of the array, from index i + 1 to the end. In the worst case, this can cover the entire array, leading to a time complexity of O(n).

The swap function runs in constant time, O(1), since it only exchanges two elements.

Therefore, the overall time complexity is O(n).


Space complexity: O(1)

The function operates in-place on the nums array, meaning no extra space is used for storing additional data.

Only a few constant space variables (i, j, and temp) are used.

The built-in swap and reverse functions do not require additional space beyond what is already present in the input array.

Hence, the space complexity is O(1)."""