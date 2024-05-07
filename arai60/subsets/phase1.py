class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []
        def recursive_find_all_subsets(subsets_so_far, index):
            if subsets_so_far not in all_subsets:
                all_subsets.append(subsets_so_far.copy())
            if nums[index] not in subsets_so_far:
                recursive_find_all_subsets(subsets_so_far + [nums[index]], index)
            index += 1
            if index < len(nums):
                recursive_find_all_subsets(subsets_so_far, index)
        recursive_find_all_subsets([], 0)
        return all_subsets