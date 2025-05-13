"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

"""

# It is a Quick Select like Quick Sort using the Pivot. Pivot is always replaced to its correct location
# At each iteration pivot is located in the exact location.
# so if the lenghth of the left sub array is k-1 then current pivot is the kth large element

#  select pivot or the last element of the array  check all other elements on the left and swap them with the
#  pivot locator if they are small
from typing import List


class Solution:
    def partition(self, left, right, array):
        pivot, pointer = array[right], left
        for i in range(left, right):
            if array[i] > pivot:
                array[i], array[pointer] = array[pointer], array[i]
                pointer += 1
        array[pointer], array[right] = array[right], array[pointer]
        return pointer

    def qq(self, left, right, array, k):
        if len(array) < 2:
            return array[k - 1]
        if left <= right:
            pivot_pointer = self.partition(left, right, array)
            if pivot_pointer == k - 1:
                return array[k - 1]
            if pivot_pointer > k - 1:
                return self.qq(left, pivot_pointer - 1, array, k)
            if pivot_pointer < k - 1:
                return self.qq(pivot_pointer + 1, right, array, k)
        return

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums=list(set(nums))
        return self.qq(0, len(nums) - 1, nums, k)

if __name__=="__main__":
    k=2
    arr = [78,2,98,3,46,90,6,2,13,50,1,37,58,4,10]
    arr= list(set(arr))
    a=Solution()
    print(a.findKthLargest(arr,k))
