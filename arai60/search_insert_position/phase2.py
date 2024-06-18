"""
hayashi-ay-san: https://github.com/hayashi-ay/leetcode/pull/40/files
.mdにあるコメントの植木算の例えがわかりやすかった。
二分探索を書く時は, https://qiita.com/DaikiSuyama/items/84df26daad11cf7da453などを参考に, 
答えの存在する範囲を狭めていくイメージで作っているけども, whileの条件文がまだうまく考えられなかったりするので参考になった。
discordのここの議論などもそれについて説明をなされていますねhttps://discord.com/channels/1084280443945353267/1192736784354918470/1199018938005213234

pythonではオーバーフローを考慮しなくて良いが、考慮する必要がある言語だと mid = left + (right - left) // 2のようにする。なども知らなかったです。

あとは計算量は言わずもがなO(logn)で, 空間計算量はnumsを保持するためにO(n)でしょうか
Runtimeは40ms~65msでした。
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if target > nums[-1]:
            # early return 
            return right + 1
        
        while left != right:

            mid = (left + right) // 2

            if nums[mid] == target:
                # ここにもearly returnを追加
                return mid
            
            elif nums[mid] < target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid
        
        return right