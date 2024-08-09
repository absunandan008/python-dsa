'''
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?
'''

class SparseVector:
    def __init__(self, nums: List[int]):
        self.pair = []
        for i,n in enumerate(nums):
            if n!=0:
                self.pair.append((i,n))


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        i = j = 0
        while i < len(self.pair) and j < len(vec.pair):
            i_idx, i_val = self.pair[i]
            j_idx, j_val = vec.pair[j]

            if i_idx == j_idx:
                result += i_val*j_val
                i += 1
                j += 1
            elif i_idx > j_idx:
                j += 1
            else:
                i += 1
        return result
