class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations_of_sum_equals_target: List[List[int]] = [] #  You will get the value of the target when all the elements of combinations are added together.
        stack = [([], 0, 0)]
        while stack:
            combinations_so_far, index_to_append, sum_so_far = stack.pop()
            # sum(combinations_so_far) == sum_so_far
            if sum_so_far == target:
                combinations_of_sum_equals_target.append(combinations_so_far)
                continue
            if sum_so_far > target:
                continue
            if index_to_append >= len(candidates):
                continue
            
            stack.append((combinations_so_far, index_to_append + 1, sum_so_far))
            append_value = candidates[index_to_append]
            stack.append((combinations_so_far + [append_value], index_to_append, sum_so_far + append_value))
        
        return combinations_of_sum_equals_target