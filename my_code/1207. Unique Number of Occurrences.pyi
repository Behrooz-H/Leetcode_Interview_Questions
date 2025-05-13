"""
1207. Unique Number of Occurrences
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
"""

from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        return len(counter.keys()) == len(set(counter.values()))
