class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        writer = 0
        for reader in range(len(nums)):
            if nums[reader] != 0:
                nums[writer],nums[reader] = nums[reader], nums[writer]
                writer += 1

    #another approach
    def moveZeroesDifferent(self, nums: List[int]) -> None:
        writer = 0
        for reader in range(len(nums)):
            if nums[reader] != 0:
                nums[writer], nums[reader] = nums[reader], nums[writer]
                writer += 1

        for i in range(writer, len(nums)):
            nums[writer] = 0
