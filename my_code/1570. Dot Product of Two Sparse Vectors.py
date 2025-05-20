""" 
1570. Dot Product of Two Sparse Vectors
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?
"""


class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []
        for index, value in enumerate(nums):
            if value != 0:
                self.pairs.append([index, value])

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        p, q = 0, 0

        while p < len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]:
                result += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            else:
                q += 1

        return result


""" 
Let n be the length of the input array and L and L 
2
​
  be the number of non-zero elements for the two vectors.

Time complexity: O(n) for creating the <index, value> pair for non-zero values; O(L+L 
2
​
 ) for calculating the dot product.

Space complexity: O(L) for creating the <index, value> pairs for non-zero values. O(1) for calculating the dot product.
"""