class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis_so_far = [1] * len(nums) # lis: longest increasing subsequence 
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j] and lis_so_far[j] < lis_so_far[i] + 1:
                    lis_so_far[j] = lis_so_far[i] + 1
        return max(lis_so_far)
