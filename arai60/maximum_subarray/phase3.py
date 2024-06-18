class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = - 10 ** 9
        min_cumulative_sum = 0
        cumulative_sum_so_far = 0
        for num in nums:
            cumulative_sum_so_far += num
            max_sum = max(max_sum, cumulative_sum_so_far - min_cumulative_sum)
            if cumulative_sum_so_far < min_cumulative_sum:
                cumulative_sum_so_far = min_cumulative_sum
        return max_sum