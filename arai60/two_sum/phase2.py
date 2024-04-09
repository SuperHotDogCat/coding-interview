from collections import defaultdict

def save_index(nums) -> Dict[int, List[int]]:
    # Save the index where the number is found.
    num2idx_map: Dict[int, List[int]] = defaultdict(list)
    for idx, number in enumerate(nums):
        num2idx_map[number].append(idx)
    return num2idx_map



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Save the index where the number is found.
        num2idx_map = save_index(nums)

        for first_idx, first_number in enumerate(nums):
            search_number = target - first_number

            if first_number == search_number:
                if len(num2idx_map[first_number]) > 1:

                    for _, idx in enumerate(num2idx_map[first_number]):
                        if idx != first_idx:

                            second_idx = idx
                            return [first_idx, second_idx]
                        
            else:
                # first_number != second_number:
                if len(num2idx_map[first_number]) == 0 or len(num2idx_map[search_number]) == 0:
                    # if at least one number was not found, continue.
                    continue
                
                second_idx = num2idx_map[search_number][0] #There is no possibility of the duplicate index, for first_number != second_number
                return [first_idx, second_idx]