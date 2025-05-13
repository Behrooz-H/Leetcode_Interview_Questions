"""
378. Kth Smallest Element in a Sorted Matrix
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2)

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
"""
import random
from typing import List


class Solution:

    def partition(self, arr, low, high, pivot_index):

        arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
        start = low  # pointer to index to perform swaps

        for i in range(low, high):
            if arr[i] < arr[high]:
                arr[i], arr[start] = arr[start], arr[i]
                start += 1

        arr[high], arr[start] = arr[start], arr[high]
        return start  # pivot

    def quickselect(self, arr, low, high, k):
        while True:
            if low == high:
                return arr[low]
            else:
                pivot_index = random.choice(range(low, high + 1))
                pindex = self.partition(arr, low, high, pivot_index)

                if pindex == k:
                    return arr[k]
                elif pindex > k:
                    high = pindex - 1
                else:
                    low = pindex + 1

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n, flat_list = len(matrix), []

        for i in range(n):
            for j in range(n):
                flat_list.append(matrix[i][j])

        return self.quickselect(flat_list, 0, len(flat_list) - 1, k - 1)
