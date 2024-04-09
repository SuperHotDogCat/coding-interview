from collections import defaultdict

def save_index(nums) -> Dict[int, List[int]]:
    # Save the index where the number is found.
    idx_map: Dict[int, List[int]] = defaultdict(list)
    for idx, number in enumerate(nums):
        idx_map[number].append(idx)
    return idx_map

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Save the index where the number is found.
        idx_map = save_index(nums)

        for first_idx, first_number in enumerate(nums):
            second_number = target - first_number

            if first_number == second_number:
                if len(idx_map[first_number]) > 1:

                    for _, idx in enumerate(idx_map[first_number]):
                        if idx != first_idx:

                            second_idx = idx

                            return [first_idx, second_idx]
            
            else:
                # first_number != second_number:
                if len(idx_map[first_number]) == 0 or len(idx_map[second_number]) == 0:
                    continue
                
                second_idx = idx_map[second_number][0]
                return [first_idx, second_idx]