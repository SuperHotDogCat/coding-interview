"""
Reference
hayashi-ayさん: https://github.com/hayashi-ay/leetcode/pull/27/files
rossy0213さん: https://github.com/rossy0213/leetcode/pull/15/files
sakupan102さん: https://github.com/sakupan102/arai60-practice/pull/32/files 二分探索のところの議論がためになりました
Exzrgsさん: https://github.com/Exzrgs/LeetCode/pull/18/files

phase1の方法の動的計画法ではなくすることで最後のmax(lis_so_far)の作業をなくすことにした。
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis_so_far = [1] * len(nums) # lis: longest increasing subsequence 
        max_lis = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis_so_far[i] = max(lis_so_far[i], lis_so_far[j] + 1)
            max_lis = max(max_lis, lis_so_far[i])
        return max_lis

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        MAX_NUM = 10 ** 4
        increasing_subsequence = [MAX_NUM + 1] * len(nums)
        for num in nums:
            index = bisect_left(increasing_subsequence, num)
            increasing_subsequence[index] = num
        return bisect_left(increasing_subsequence, MAX_NUM + 1)
