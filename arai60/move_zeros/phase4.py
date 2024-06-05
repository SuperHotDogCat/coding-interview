class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[non_zero_length], nums[i] = nums[i], nums[non_zero_length]
            non_zero_length += 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_length = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_length] = nums[i]
                non_zero_length += 1
        for i in range(non_zero_length, len(nums)):
            nums[i] = 0
