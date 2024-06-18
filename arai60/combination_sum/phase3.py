class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 書くのが安定しているwhileで書く
        combinations = []
        stack = [[[], 0, 0]] # current_combination, current_index, current_value
        while stack:
            current_combination, current_index, current_value = stack.pop()
            if current_value == target:
                combinations.append(current_combination)
                continue
            
            if current_value > target:
                continue
            
            if current_index >= len(candidates):
                continue
            
            stack.append([current_combination, current_index + 1, current_value])
            added_current_combination = current_combination.copy()
            added_current_combination.append(candidates[current_index])
            stack.append([added_current_combination, current_index, current_value + candidates[current_index]])
        
        return combinations