'''
A permutation of an array of integers is an arrangement of
its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of
arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
'''

class Solution:
    def reverse_array(self, index, nums):
        #remember to increase index for lo range
        lo = index + 1
        hi = len(nums) - 1
        while lo < hi:
            nums[lo],nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1

        # first go from end to begining, if u find something whose next is smaller
        # [1,2,3, 1, 5,4,3,0,0] -- talking about 1 here
        # then that mean we have found a prefix where the next element we can change -
        # so we will change 1 with 3 -- [123 3 54 1 00]
        # to find new permutaion. This also mean numbers after the index we have found is
        # all are larger and sorted. But if we did find an index then just reverse the nums [123 3 1 4500]

        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                index = i
                break

        if index == -1:
            return nums.reverse()
        for i in range(len(nums)-1, index, -1):
            if nums[index] < nums[i]:
                #remember to swap the index with the higher one
                nums[index], nums[i] = nums[i], nums[index]
                self.reverse_array(index, nums)
                break
