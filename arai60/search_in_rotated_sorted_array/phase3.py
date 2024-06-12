import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def _find_minimum_index():
            # 二分探索でnumsの最小値のindexを見つける
            left = 0
            right = len(nums) - 1
            while left != right:
                mid = (left + right) // 2
                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid + 1
            return right
        
        min_index = _find_minimum_index()
        if nums[min_index] <= target <= nums[-1]:
            left = min_index
            right = len(nums)
        else:
            left = 0
            right = min_index
        
        target_index = bisect.bisect_left(nums, target, left, right)
        if nums[target_index] == target:
            return target_index
        return -1