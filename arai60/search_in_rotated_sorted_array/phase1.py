# 最小値のindexを見つけてそこで左右に分割して考えると分割したところは増加列になっていることを利用する
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def _find_minimum_index():
            # 最小値の数がどこにあるかをO(logN)で見つける
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
            right = len(nums) - 1
        else:
            left = 0
            right = min_index - 1
        
        # targetを探す
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        
        if nums[right] == target:
            return right
        return -1