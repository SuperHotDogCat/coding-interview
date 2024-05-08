class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []
        def find_all_subsets(begin, current_subset):
            all_subsets.append(current_subset[:])
            for i in range(begin, len(nums)):
                current_subset.append(nums[i])
                find_all_subsets(i+1, current_subset)
                current_subset.pop()
        find_all_subsets(0, [])
        return all_subsets