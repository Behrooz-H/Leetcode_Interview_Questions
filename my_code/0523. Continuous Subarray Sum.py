"""
523. Continuous Subarray Sum

Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
A good subarray is a subarray where:

-its length is at least two, and
-the sum of the elements of the subarray is a multiple of k.
Note that:
A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
"""

class Solution:
    def checkSubarraySum(self, nums, k):
        prefix_mod = 0
        mod_seen = {0: -1}

        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k

            if prefix_mod in mod_seen:
                # ensures that the size of subarray is at least 2
                if i - mod_seen[prefix_mod] > 1:
                    return True
            else:
                # mark the value of prefix_mod with the current index.
                mod_seen[prefix_mod] = i

        return False
    
    
    """
Time = O(N) We iterate through the array exactly once. In each iteration, we perform a search operation in the hashmap that takes O(1) time. 
Therefore, the time complexity can be stated as O(n).

Space complexity: O(n)
In each iteration, we insert a key-value pair in the hashmap. 
The space complexity is O(n) because the size of the hashmap is proportional to the size of the list after n iterations.
    Space = O(N)
    """