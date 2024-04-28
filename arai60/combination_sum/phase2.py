"""
Reference
hayashi-ay: https://github.com/hayashi-ay/leetcode/pull/65/files
shining-ai: https://github.com/shining-ai/leetcode/pull/52/files
phase1の方法だと重複する場合が出てきた分だけ状態数も増えていることに気づいた。
indexを増やすか今のindexが指す値を足すかで場合分けすれば十分であることがわかった。
あと現在の足し込んだ値がtargetより大きいかで判断した方が多分素直な実装ですね(phase1でcurrent_target - candidates[current_candidate_index] >= 0と書いていた)

あとは, 
make_combination(index + 1, current_sum)
partial_combination.append(candidates[index])
make_combination(index, current_sum + candidates[index])
partial_combination.pop()
のような再帰を考えたことはなかったですね, これで再帰関数の引数から現在のcombinationを入れなくて済むんですね

Mike0121: https://github.com/Mike0121/LeetCode/pull/1/files
時間計算量が分割数というらしい
"""

# 再帰, whileの2通りで書く
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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

# 再帰
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        partial_combination = []
        def make_combinations(index: int, total: int) -> None:
            if total == target:
                combinations.append(partial_combination.copy())
                return

            if total > target:
                return 

            if index >= len(candidates):
                return

            make_combinations(index + 1, total)
            partial_combination.append(candidates[index])
            make_combinations(index, total + candidates[index])
            partial_combination.pop()
        
        make_combinations(0, 0)
        return combinations