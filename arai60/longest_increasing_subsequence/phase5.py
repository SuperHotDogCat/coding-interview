class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis_so_far = []
        for num in nums:
            index = bisect.bisect_left(lis_so_far, num)
            if index == len(lis_so_far):
                lis_so_far.append(num)
            elif index < len(lis_so_far):
                lis_so_far[index] = num
        return len(lis_so_far)
