'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1. To accommodate this,
nums1 has a length of m + n,
where the first m elements denote the elements
that should be merged, and the last n elements are set to 0
and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
'''
import unittest
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n!=0:
            if m!=0 and nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -=1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1


class TestMergeSortedArrays(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def run_test(self, nums1, m, nums2, n, expected):
        print(f"\nInput:")
        print(f"nums1 = {nums1}, m = {m}")
        print(f"nums2 = {nums2}, n = {n}")

        self.solution.merge(nums1, m, nums2, n)

        print(f"Output: {nums1}")
        print(f"Expected: {expected}")

        self.assertEqual(nums1, expected)

    def test_example1(self):
        self.run_test([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6])

    def test_example2(self):
        self.run_test([1], 1, [], 0, [1])

    def test_example3(self):
        self.run_test([0], 0, [1], 1, [1])

    def test_empty_nums1(self):
        self.run_test([0, 0, 0], 0, [1, 2, 3], 3, [1, 2, 3])

    def test_empty_nums2(self):
        self.run_test([1, 2, 3], 3, [], 0, [1, 2, 3])


if __name__ == '__main__':
    unittest.main(verbosity=2)