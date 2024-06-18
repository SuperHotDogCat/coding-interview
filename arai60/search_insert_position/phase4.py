from typing import List

class Solution:
    # 今回の問題ではnumsがdistinctなので起こり得ないが, 同じ数が含まれている時に代入すべき左端のindexを出すことにした
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                # nums[mid] >= target
                right = mid
                
        return right

s = Solution()
nums = [1,1,1,1,5,5,5,5,7,7,7,]
print(s.searchInsert(nums,5)) 
print(s.searchInsert(nums,7))
print(s.searchInsert(nums,1))