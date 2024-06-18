from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 再帰でも解けそうな気がするが, ひとまず単純な探索で解く

        stack = [[[], 0, target]] # [current_combination, current_candidate_index, current_target] 
        combinations = []
        while stack:
            current_combination, current_candidate_index, current_target = stack.pop()

            if current_target == 0 and current_combination not in combinations:
                combinations.append(current_combination)
                continue

            if current_target - candidates[current_candidate_index] >= 0:
                tmp_current_combination = current_combination.copy() # copy
                tmp_current_combination.append(candidates[current_candidate_index])
                stack.append([tmp_current_combination, current_candidate_index, current_target - candidates[current_candidate_index]])
            
            if current_candidate_index + 1 < len(candidates) and current_target - candidates[current_candidate_index+1] >= 0:
                tmp_current_combination = current_combination.copy() # copy
                tmp_current_combination.append(candidates[current_candidate_index+1])
                stack.append([tmp_current_combination, current_candidate_index+1, current_target - candidates[current_candidate_index+1]])
            
            if current_candidate_index + 1 < len(candidates):
                tmp_current_combination = current_combination.copy() # copy
                stack.append([tmp_current_combination, current_candidate_index+1, current_target])
        
        return combinations