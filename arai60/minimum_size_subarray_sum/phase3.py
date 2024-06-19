class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sum = [0] * (len(nums)+1)
        for i in range(1, len(nums) + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        left = 0
        right = 0
        min_length = len(nums) + 1
        while right < len(prefix_sum):
            if target <= prefix_sum[right]-prefix_sum[left]:
                min_length = min(min_length, right - left)
                left += 1
            else:
                right += 1

        if min_length == len(nums)+1:
            return 0
        return min_length
