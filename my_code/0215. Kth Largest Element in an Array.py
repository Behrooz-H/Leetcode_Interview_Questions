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

#*TODO **** IMPORTANT NOTE 
#! 1-First Approch One(1) is sorting and returning kth ->Olog(N) and O 

#? 2-Second Approach TWO (2) is using and push all into MaxHeap and pop k times or more efficien is using Minheap to find Kth 
# largest item. Easily push items into a min heap and monitor its size, if its size is more than k, remove its root, It
# will keep the largest in its leafs and after traversing all elements, its root will be Kth smallest among all othrs wich are 
# bigger, so root is the 

# NOTE: 4- Fourth  Approach is  counting in a dictionary but instead of a dictionary use an array to save the Kth element in the array which is not zero



#Third Approach  Quick selectlike quick sort    
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

# This solution is optimal 




# _Fourth Approach_________________________________________
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_value = min(nums)
        max_value = max(nums)
        count = [0] * (max_value - min_value + 1)

        for num in nums:
            count[num - min_value] += 1
        
        remain = k
        for num in range(len(count) -1, -1, -1):
            remain -= count[num]
            if remain <= 0:
                return num + min_value

        return -1
# This solution is still occupying a large memory here  if distance between max_value and min_value is near large scale
"""Time complexity: O(n+m)
We first find maxValue and minValue, which costs O(n).
Next, we initialize count, which costs O(m).
Next, we populate count, which costs O(n).
Finally, we iterate over the indices of count, which costs up to O(m).

Space complexity: O(m). We create an array count with size O(m).  
"""
# _________________________________________________________

    
if __name__=="__main__":
    k=2
    arr = [78,2,98,3,46,90,6,2,13,50,1,37,58,4,10]
    arr= list(set(arr))
    a=Solution()
    print(a.findKthLargest(arr,k))
