"""
Reference:
fhiyo: https://github.com/fhiyo/leetcode/pull/19/files
hayashi-ay: https://github.com/hayashi-ay/leetcode/pull/31/files
Exzrgs: https://github.com/Exzrgs/LeetCode/commit/caa03ede122e5e1d2de4b8ebd24ee26aaf3d743b

なんか前も先にindexを保存しておくかfor文の中で動的に処理するかみたいなので先にindexを保存したせいで沼にハマった問題をやった記憶があるな...?
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_to_frequency = defaultdict(int) # sum(nums[:i]): frequency
        prefix_sum_to_frequency[0] = 1
        prefix_sum = 0 # sum(nums[:i])
        count = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            count += prefix_sum_to_frequency[prefix_sum - k]
            prefix_sum_to_frequency[prefix_sum] += 1
        return count
