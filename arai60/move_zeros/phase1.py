class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0のある幅をleftとrightにし, swapするたびにleft側を狭めていくイメージの解答
        index = 0
        left = len(nums)
        while index < len(nums):
            if nums[index] != 0:
                index += 1
                continue
            left = min(index, left)
            right = index
            while right < len(nums) and nums[right] == 0:
                right += 1
            if right < len(nums):
                nums[left], nums[right] = nums[right], nums[left]
            index = right
            left = left + 1