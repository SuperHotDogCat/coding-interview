"""
Reference
fhiyo: https://github.com/fhiyo/leetcode/pull/25/files if not の場合早期returnすることができる(新しいのを作らなくても済むのでGood)
sakupan: https://github.com/sakupan102/arai60-practice/pull/24/files
hayashi-ay: https://github.com/hayashi-ay/leetcode/pull/12/files

>>>
新しいのを作るか作らないのか、古い入力を壊すのか壊さないのか、共有するのかしないのか(変更しない前提ならばメモリー使用量が減る)、などのオプションがあって、自分がどれを「選択」したかを意識しましょう。

入力を破壊している。
https://discord.com/channels/1084280443945353267/1252267683731345438/1252556045524537344
出力を変更されるとキャッシュが変わって次からの呼び出しが狂う。
https://discord.com/channels/1084280443945353267/1252267683731345438/1252591437485441024

phase1ではroot1のメモリ領域を使うイメージで作った。新しくTreeを作るイメージの時はまた別の書き方の方が良い
"""

# root1に統合
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        elif not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

# 新しくtreeを生成
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return copy.deepcopy(root2)
        elif not root2:
            return copy.deepcopy(root1)
        merged_tree = TreeNode(root1.val + root2.val)
        merged_tree.left = self.mergeTrees(root1.left, root2.left)
        merged_tree.right = self.mergeTrees(root1.right, root2.right)
        return merged_tree
