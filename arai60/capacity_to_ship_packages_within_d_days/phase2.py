"""
Reference
YukiMichishita: https://github.com/YukiMichishita/LeetCode/pull/10/files
shining-ai: https://github.com/shining-ai/leetcode/pull/44/files
hayashi-ay: https://github.com/hayashi-ay/leetcode/pull/55/files
is_possibleだと何がpossibleかわかりにくいのでcanbe_shippedへ変更, valid_capacity,invalid_capacityという命名にしていたが
low, highぐらいの命名へ, 二分探索はこれぐらいの名前の重さの方が伝わりやすい?
"""

# 命名をcan_be_shippedに, 探索範囲を狭めることで無駄なif文を削除へ

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low < high:
            middle = (low + high) // 2
            if self._can_be_shipped(weights, days, middle):
                high = middle
            else:
                low = middle + 1
        return high
    
    def _can_be_shipped(self, weights: List[int], days: int, capacity: int):
        # Ensure max(weights) <= capacity
        spent_days = 1
        current_weight = 0
        for weight in weights:
            if current_weight + weight > capacity:
                spent_days += 1
                current_weight = 0
            if spent_days > days:
                return False
            current_weight += weight
        return True
