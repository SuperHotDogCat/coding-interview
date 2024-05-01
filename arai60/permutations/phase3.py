class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        all_permutations: List[List[int]] = []
        def make_permutations(candidates: List[int]):
            if len(candidates) == len(nums):
                all_permutations.append(candidates.copy())
                return
            for num in nums:
                if num in candidates:
                    continue
                candidates.append(num)
                make_permutations(candidates)
                candidates.pop() # backtrack
        
        make_permutations([])
        return all_permutations