class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis_so_far = [1] * len(nums) # lis means longest increasing subsequence
        max_lis = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis_so_far[i] = max(lis_so_far[i], lis_so_far[j] + 1)
        return max(lis_so_far)
