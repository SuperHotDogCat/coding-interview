"""
Reference
shining-aiさん: https://github.com/shining-ai/leetcode/pull/33/files 
hayashi-ayさん: https://github.com/hayashi-ay/leetcode/pull/36/files
phase1のコードが何やってるのか一番わかりやすかったが, 1loopで書くとやはりちょっと可読性は下がるかという印象。

# indexまでの要素を使った最大値
current_sum_subarray = nums[0]
max_sum_subarray = nums[0]
current_sum_subarray = max(current_sum_subarray + nums[i], nums[i])
max_sum_subarray = max(max_sum_subarray, current_sum_subarray)
のところの解読にやや時間がかかった。
max(current_sum_subarray + nums[i], nums[i])でnums[i]が採択されるようならば, 
今までのcurrent_sum_subarrayはそれ以降のcumsumにとって負の影響しか残さないから捨てた方が良いという感じだろうか
ex.
nums:                           [-2, 1,-3,4,-1,2,1,-5,4]
cumsum:                         [-2,-1,-4,0,-1,1,2,-3,1]
current_sum_subarrayの採用する値  [-2, 1,-2,4, 3,5,6, 1,5]

調べてみたところKadane's Algorithmというアルゴリズムらしい
ある地点までのmax(ある地点までの最大部分配列和 + ある地点の値, ある地点の値)というアルゴリズムになっている
"""

# 変数名など手直し
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_cumulative_sum = 0 # The minimum of the cumulative sum of nums
        cumulative_sum_so_far = 0 
        max_sum = - 10 ** 9
        for num in nums:
            cumulative_sum_so_far += num
            max_sum = max(max_sum, cumulative_sum_so_far - min_cumulative_sum)
            if cumulative_sum_so_far < min_cumulative_sum:
                min_cumulative_sum = cumulative_sum_so_far
        return max_sum

# Divide and conquer
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # divide and conquer
        def calculate_max_sum_subarray(nums: List[int], left: int, right: int) -> int:
            if left > right:
                return - 10 ** 9
            mid = (left + right) // 2
            left_sum = 0
            right_sum = 0
            temporary_sum = 0 # variable to save the temporary sum of both left and right
            for i in range(mid-1, left-1, -1):
                temporary_sum += nums[i]
                left_sum = max(left_sum, temporary_sum)
            temporary_sum = 0
            for i in range(mid+1, right+1):
                temporary_sum += nums[i]
                right_sum = max(right_sum, temporary_sum)
            
            return max(
                calculate_max_sum_subarray(nums, left, mid-1), 
                calculate_max_sum_subarray(nums, mid+1, right), 
                left_sum + nums[mid] + right_sum
            )
        
        return calculate_max_sum_subarray(nums, 0, len(nums) - 1)