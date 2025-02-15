# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_traversed_node_ids = []
        def append_by_depth(node: Optional[TreeNode], depth: int):
            if not node:
                return
            if len(level_traversed_node_ids) == depth:
                level_traversed_node_ids.append([])
            
            level_traversed_node_ids[depth].append(node.val)
            append_by_depth(node.left, depth + 1)
            append_by_depth(node.right, depth + 1)

        append_by_depth(root, 0)
        return level_traversed_node_ids
