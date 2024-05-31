"""
Reference:
shining-aiさん: https://github.com/shining-ai/leetcode/pull/54/files
non_zeroではない要素を代入し, 最後に0をいれるアルゴリズムで賢い, in-placeな処理も満たされてて良い
hayashi-ayさん: https://github.com/hayashi-ay/leetcode/pull/58/files
shining-aiさんと同じような解答, こちらがソフトウェアエンジニアらしくはあるのかなと思う

2種類で書く。最初はloop内部でswapするもの, もう一つは最後に0埋めするもの
"""

# ループ不変式, nums[0], nums[1], nums[2], ..., nums[non_zero_index-1]までが0ではない
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1

# 最後に0埋め
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            # nums[i] != 0
            nums[non_zero_index] = nums[i]
            non_zero_index += 1
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0