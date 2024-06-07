# book allocation problemと言うらしい
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        invalid_capacity = 0
        valid_capacity = sum(weights)
        while invalid_capacity < valid_capacity:
            mid_capacity = (valid_capacity + invalid_capacity) // 2
            if self._is_possible(weights, days, mid_capacity):
                valid_capacity = mid_capacity
            else:
                invalid_capacity = mid_capacity + 1
        return valid_capacity
    
    def _is_possible(self, weights: List[int], days: int, capacity: int):
        spent_days = 1
        current_weight = 0
        for weight in weights:
            if weight > capacity:
                return False
            elif current_weight + weight > capacity:
                spent_days += 1
                current_weight = weight
            else:
                current_weight += weight
            if spent_days > days:
                return False
        return True
