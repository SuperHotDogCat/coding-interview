class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def _find_pivot_index(nums: List[int])->int:
            # 比較の中心となるindexを定義
            # 末端から見ていって増加関係のないところを比較indexとする
            pivot_index = len(nums) - 2 
            while pivot_index > -1 and nums[pivot_index] >= nums[pivot_index+1]:
                pivot_index -= 1
            return pivot_index
        
        def _find_swap_index(nums: List[int], pivot_index: int)->int:
            # swapに使うindexを定義
            # swapする位置のindexを求める
            swap_index = len(nums) - 1 
            while nums[swap_index] <= nums[pivot_index]:
                swap_index -= 1
            return swap_index

        if len(nums) == 1:
            return
        
        pivot_index = _find_pivot_index(nums)
        
        if pivot_index == -1:
            nums.reverse()
            return
        
        swap_index = _find_swap_index(nums, pivot_index)
        
        nums[swap_index], nums[pivot_index] = nums[pivot_index], nums[swap_index]

        nums[pivot_index+1:] = reversed(nums[pivot_index+1:])
        return

"""
None型を返すせいで, 正直PythonよりはC++とかの方が書きやすいと感じたが, とりあえずPythonで書く練習をした

Reference:
https://github.com/shining-ai/leetcode/pull/58/files 解くことに夢中になりすぎて関数での分割を忘れていた。
nums[pivot_index+1:] = reversed(nums[pivot_index+1:])よりもnums[left + 1 :] = sorted(nums[left + 1 :])
の方が認知コストは低いなあと感じた。reversedで良いことは紙とペンで確かめられるけど, それをしなきゃいけない感じのコードなら確かに書くべきではないのかも

https://github.com/hayashi-ay/leetcode/pull/67/files 
markdownに書いてあるNext Permutationアルゴリズムの説明がわかりやすいと思いました。あとコメントにあった通り次から関数名は動詞から書き始めることを意識してみます。
"""