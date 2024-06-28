# 再帰の解き方
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        def traverse_nodes(node, depth):
            # node: the node you concentrate on
            # depth: the depth of the node you concentrate on
            nonlocal max_depth
            if node == None:
                return
            if max_depth < depth:
                max_depth = depth
            traverse_nodes(node.left, depth + 1)
            traverse_nodes(node.right, depth + 1)

        traverse_nodes(root, 1)
        return max_depth
