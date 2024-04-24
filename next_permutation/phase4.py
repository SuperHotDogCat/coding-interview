class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def _find_first_not_sorted_index(nums: List[int])->int:
            # 後ろから走査し, nums[index] >= nums[index+1]ではなくなる初めてのindexを取り出す
            index = len(nums) - 2
            while index > -1 and nums[index] >= nums[index+1]:
                index -= 1
            return index
        
        def _find_second_largest_index(nums: List[int], compare_index: int)->int:
            # 後ろからnums[compare_index]より大きい数を見つけてswapするindexを取り出す
            index = len(nums) - 1
            while nums[index] <= nums[compare_index]:
                index -= 1
            return index
        
        if len(nums) == 1:
            return
        
        left = _find_first_not_sorted_index(nums)

        if left == -1:
            nums.reverse()
            return 
        
        right = _find_second_largest_index(nums, left)

        nums[right], nums[left] = nums[left], nums[right]

        nums[left+1:] = sorted(nums[left+1:])

        return nums