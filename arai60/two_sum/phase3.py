from collections import defaultdict

def save_index(nums: List[int]) -> Dict[int, List[int]]:
    num2idx_map: Dict[int, List[int]] = defaultdict(list)
    for idx, num in enumerate(nums):
        num2idx_map[num].append(idx)
    return num2idx_map

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # save the index where the number is found.
        num2idx_map = save_index(nums)

        for first_idx, first_number in enumerate(nums):
            search_number = target - first_number

            if search_number == first_number:
                # There is possibility of duplicate numbers
                if len(num2idx_map[first_number]) < 2:
                    continue
                else:
                    #len(num2idx_map[first_number]) >= 2
                    for idx in num2idx_map[first_number]:
                        if idx != first_idx:
                            second_idx = idx
                            return [first_idx, second_idx]
            
            else:
                #search_number != first_number
                if len(num2idx_map[first_number]) == 0 or len(num2idx_map[search_number]) == 0:
                    continue
                
                second_idx = num2idx_map[search_number][0]
                return [first_idx, second_idx]