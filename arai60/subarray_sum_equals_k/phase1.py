# 奇跡的にギリギリTLEしないコードです
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_sum = [0] * (len(nums) + 1)
        cumulative_sum_to_index = defaultdict(list)
        cumulative_sum_to_index[0].append(0)
        for i in range(1, len(nums) + 1):
            cumulative_sum[i] = cumulative_sum[i - 1] + nums[i - 1]
            cumulative_sum_to_index[cumulative_sum[i]].append(i)
        
        count = 0
        for i in range(len(nums) + 1):
            for j in cumulative_sum_to_index[cumulative_sum[i] - k]:
                if j < i:
                    count += 1
        return count
