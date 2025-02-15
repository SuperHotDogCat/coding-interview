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
            node_ids = []
            next_level_nodes = []
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
