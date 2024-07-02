"""
Reference:
fhiyo: https://github.com/fhiyo/leetcode/pull/27/files
sakupan102: https://github.com/sakupan102/arai60-practice/pull/26#discussion_r1593805972

・phase1ではtargetSumを更新して0かどうかを判断していたが, 葉だったらtargetSum == root.valかどうかを返してそれ以外はrest = targetSum - root.valとして処理する方が好みだったので書き換える。
・|演算子よりかはor演算子の方が良いか(|はビット演算子, orの方がboolを扱う時の方では馴染みがありそう...?)
"""

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.right and not root.left:
            return targetSum == root.val
        rest = targetSum - root.val # update targetSum
        return self.hasPathSum(root.right, rest) or self.hasPathSum(root.left, rest)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        stack = [(root, targetSum)]
        while stack:
            node, current_sum = stack.pop()
            if not node:
                continue
            if not node.right and not node.left and node.val == current_sum:
                return True
            
            rest = current_sum - node.val
            stack.append((node.right, rest))
            stack.append((node.left, rest))
        return False
