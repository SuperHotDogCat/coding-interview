class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        adding_number = nums.pop()
        added_permutations = self.permute(nums) # permutations without adding_number
        permutations: List[List[int]] = [] # all the pattern of the permutations of nums
        for added_permutation in added_permutations:
            for i in range(len(added_permutation)+1):
                permutations.append(added_permutation[:i] + [adding_number] + added_permutation[i:]) 
                # insert adding_number as i-th number of added_permutations
        
        return permutations