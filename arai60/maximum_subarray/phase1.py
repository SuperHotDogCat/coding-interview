class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 今まで確認してきた区間の中で最小のcumsumから, 最高の値のcumsumを引けば良い。
        # 最小のcumsumの初期数値を0にすることで最後のcumsumが最大となるパターンにも対応できる
        min_cumulative_sum = 0 # The minimum of the cumulative sum of nums
        cumulative_sum_so_far = 0 
        max_subarray_sum = - 10 ** 9
        for num in nums:
            cumulative_sum_so_far += num
            max_subarray_sum = max(max_subarray_sum, cumulative_sum_so_far - min_cumulative_sum)
            if cumulative_sum_so_far < min_cumulative_sum:
                min_cumulative_sum = cumulative_sum_so_far
        return max_subarray_sum