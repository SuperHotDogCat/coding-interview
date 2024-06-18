class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def _find_pivot_index(nums: List[int])->int:
            # 比較の対象となる数のindexを見つける
            pivot_index = len(nums) - 2
            while pivot_index > -1 and nums[pivot_index] >= nums[pivot_index+1]:
                pivot_index -= 1
            return pivot_index
        
        def _find_swap_index(nums: List[int], pivot_index: int)->int:
            # 後ろからnums[pivot_index]より大きい数を見つけてswapするindexを取り出す
            swap_index = len(nums) - 1
            while nums[swap_index] <= nums[pivot_index]:
                swap_index -= 1
            return swap_index
        
        if len(nums) == 1:
            return
        
        pivot_index = _find_pivot_index(nums)

        if pivot_index == -1:
            nums.reverse()
            return 
        
        swap_index = _find_swap_index(nums, pivot_index)

        nums[swap_index], nums[pivot_index] = nums[pivot_index], nums[swap_index]

        nums[pivot_index+1:] = sorted(nums[pivot_index+1:])

        return nums