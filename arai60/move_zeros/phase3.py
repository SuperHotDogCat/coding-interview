class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[non_zero_index] = nums[i]
            non_zero_index += 1
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0
