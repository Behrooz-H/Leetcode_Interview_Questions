""" 
1539. Kth Missing Positive Number

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

"""

class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            # missing count before arr[mid]
            missing = arr[mid] - (mid + 1)
            
            if missing < k:
                left = mid + 1
            else:
                right = mid - 1
        
        # The kth missing number is to the right of arr[right]
        return left + k
""" 
⏱️ Time Complexity:
O(log n) — Binary search over the array

🧠 Space Complexity:
O(1) — Constant space used
"""