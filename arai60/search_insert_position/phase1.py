class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        if target > nums[-1]:
            # early return 
            return right + 1
        
        while left != right:
            compare_index = (left + right) // 2

            if nums[compare_index] < target:
                left = compare_index + 1
            
            elif nums[compare_index] >= target:
                right = compare_index
        
        return right

# オマケ: ズルしてみる
import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)