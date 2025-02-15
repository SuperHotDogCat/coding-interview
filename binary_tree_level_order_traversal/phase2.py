# レベルごとの捜査なのでBFSが適しているというコメントがあり, そりゃそうだわの気持ちになり反省
# 再帰で書く変な先入観みたいなのがついている気がしたので今一度なんで書くのかをしっかりと...
# seal-azarashi: https://github.com/seal-azarashi/leetcode/pull/25/files
# goto-untrapped: https://github.com/goto-untrapped/Arai60/pull/50/files
# Ryotaro25: https://github.com/Ryotaro25/leetcode_first60/pull/28/files
# BFSで解くこと, 一つの変数に二つの役割を持たさないように注意して再度実行

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_to_nodes = []
        current_level_nodes = [root]
        while current_level_nodes:
            next_level_nodes = []
            node_ids = []
            for node in current_level_nodes:
                if not node:
                    continue
                node_ids.append(node.val)
                next_level_nodes.append(node.left)
                next_level_nodes.append(node.right)
            
            current_level_nodes = next_level_nodes
            if len(node_ids) > 0:
                level_to_nodes.append(node_ids)

        return level_to_nodes
