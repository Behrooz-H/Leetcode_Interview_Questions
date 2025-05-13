"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

"""

"""
Start from each end and calculate the maximum area
"""

# Computation: O(N) , Space = O(1)

from  typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea, left, right = 0,0,len(height) - 1

        while left < right:
            maxarea = max(maxarea, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxarea


def Second_max_container(arr: list):
    first, last, max = 0, len(arr) - 1, 0
    while first < last:
        tmp = (last - first) * min(arr[first], arr[last])
        print(f"first:{first}-->value {arr[first]},  last: {last} --> value {arr[last]},tmp: {tmp}")
        max = tmp if tmp > max else max
        if arr[first] < arr[last]:
            first += 1
        else:
            last += 1
    return max


arr = [2, 3, 4, 8, 9, 5, 7, 10, 13, 1, 22, 35]
find_max_container(arr)
