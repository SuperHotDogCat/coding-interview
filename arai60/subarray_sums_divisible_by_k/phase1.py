class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remain_to_counts = defaultdict(int)
        remain_to_counts[0] = 1
        count = 0
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            remain = prefix_sum % k
            count += remain_to_counts[remain] 
            # 累積和の引き算の余りはここまでの累積和の余りの引き算で良い, なので同じremainがここまで現れたかを計上する
            remain_to_counts[remain] += 1
        return count
