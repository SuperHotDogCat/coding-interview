"""
Reference
hayashi-ay: https://github.com/hayashi-ay/leetcode/pull/51/files
shining-ai: https://github.com/shining-ai/leetcode/pull/49/files
mike: https://github.com/Mike0121/LeetCode/pull/22/files
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sum = [0] * (len(nums)+1)
        for i in range(1, len(nums) + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        
        left = 0
        right = 0
        min_length = len(nums) + 1
        while right < len(prefix_sum):
            # phase1のtarget > prefix_sum[right] - prefix_sum[left]はなんだか素直じゃない, 
            # 問題文にreturn the minimal length of a subarray whose sum is greater than or equal to targetとあるのだからそうすべき
            if target <= prefix_sum[right]-prefix_sum[left]:
                min_length = min(min_length, right - left)
                left += 1
            else:
                right += 1

        if min_length == len(nums)+1:
            return 0
        return min_length

# 配列を使わずに解く練習
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sum = 0
        min_length = len(nums) + 1 
        left = 0
        right = 0
        while right < len(nums):
            prefix_sum += nums[right]
            while prefix_sum >= target:
                min_length = min(min_length, right - left + 1)
                prefix_sum -= nums[left]
                left += 1
            right += 1
            
        if min_length == len(nums)+1:
            return 0
        return min_length
