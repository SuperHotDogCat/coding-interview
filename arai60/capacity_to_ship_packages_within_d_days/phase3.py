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
    
    def _can_be_shipped(self, weights: List[int], days: int, capacity: int) -> bool:
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
