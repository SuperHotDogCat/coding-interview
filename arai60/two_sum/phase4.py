class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_to_index = {} # map: already_seen_number -> index
        for index, number in enumerate(nums):
            complement_number = target - number
            if complement_number in number_to_index:
                return [number_to_index[complement_number], index]
            number_to_index[number] = index
        raise Exception("Unreachable")