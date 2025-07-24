"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

def trap(arr):
    if len(arr) <= 2:
        return 0
    else:
        right, left , total = len(arr)-1, 0 ,0
        max_right = arr[right]
        max_left = arr[left]
        while right > left:
            if max_right < max_left:
                right -= 1
                if right > left:
                    if max_right > arr[right]:
                        total += max_right-arr[right]
                    else:
                        max_right = arr[right]
            else:
                left += 1
                if left < right:
                    if max_left > arr[left]:
                        total += max_left - arr[left]
                    else:
                        max_left = arr[left]
        return total


"""
Time = O(N)
Space = O(1)
"""

 # arr=[0,1,0,2,1,0,3,1,0,1,2]









