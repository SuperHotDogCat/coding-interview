class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        
        pivot_index = len(nums) - 2 # 比較の中心となるindexを定義
        while pivot_index > -1 and nums[pivot_index] >= nums[pivot_index+1]:
            pivot_index -= 1
        
        if pivot_index == -1:
            nums.reverse()
            return
        
        swap_index = len(nums) - 1 # swapに使うindexを定義
        while nums[swap_index] <= nums[pivot_index]:
            swap_index -= 1
        
        nums[swap_index], nums[pivot_index] = nums[pivot_index], nums[swap_index]

        nums[pivot_index+1:] = reversed(nums[pivot_index+1:])
        return
