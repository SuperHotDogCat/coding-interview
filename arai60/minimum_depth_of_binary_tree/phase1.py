class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 幅優先で良い
        minimum_depth = 0
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if not node:
                minimum_depth = depth
                break
            if node.right and node.left:
                queue.append((node.right, depth + 1))
                queue.append((node.left, depth + 1))
            elif node.right is not None:
                queue.append((node.right, depth + 1))
            else:
                queue.append((node.left, depth + 1))
        return minimum_depth
