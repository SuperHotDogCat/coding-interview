"""
Reference:
fhiyo: https://github.com/fhiyo/leetcode/pull/24/files
rossy0213: https://github.com/rossy0213/leetcode/pull/11/files
hayashi-ay: https://github.com/hayashi-ay/leetcode/pull/26
shining-ai: https://github.com/shining-ai/leetcode/pull/22/files
"""

# if文を簡潔に改善, 枝葉の判定をnode.right, node.leftどちらもnoneの時にすることに
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # 幅優先で良い
        minimum_depth = 0
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.right and not node.left:
                # 枝葉
                minimum_depth = depth
                break # ここで早期returnしてしまって, while文を抜けたらraise Exception("unreachable")する手もある(hayashi-ayさん)
            if node.right:
                queue.append((node.right, depth + 1))
            if node.left:
                queue.append((node.left, depth + 1))

        return minimum_depth

# 再帰で深さ優先探索
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.right:
            return self.minDepth(root.left) + 1
        if not root.left:
            return self.minDepth(root.right) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
