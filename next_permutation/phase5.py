class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def _find_first_not_sorted_index() -> int:
            index = len(nums) - 2
            while index >= 0 and nums[index] >= nums[index+1]:
                index -= 1
            return index
        
        def _rfind_bigger_than(compare_index: int) -> int:
            index = len(nums) - 1
            while nums[index] <= nums[compare_index]:
                index -= 1
            return index

        left = _find_first_not_sorted_index()

        if left == -1:
            nums.reverse()
            return 
        
        right = _rfind_bigger_than(left)
        nums[left], nums[right] = nums[right], nums[left]
        nums[left+1:].reverse()
        return 