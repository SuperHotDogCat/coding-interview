class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_to_frequency = defaultdict(int) # sum(nums[:i]): frequency
        prefix_sum_to_frequency[0] = 1 # sum(nums[:0]): 1
        prefix_sum = 0
        count = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            count += prefix_sum_to_frequency[prefix_sum - k]
            prefix_sum_to_frequency[prefix_sum] += 1
        return count 
