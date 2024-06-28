class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        def traverse(node: Optional[TreeNode], depth: int) -> None:
            # node: the node you concentrate on
            # depth: the depth of the node you concentrate on
            nonlocal max_depth
            if node is None:
                return
            if max_depth < depth:
                max_depth = depth
            traverse(node.right, depth + 1)
            traverse(node.left, depth + 1)
        
        traverse(root, 1)
        return max_depth
