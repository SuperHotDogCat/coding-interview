"""
Reference
fhiyo: https://github.com/fhiyo/leetcode/pull/23/files phase1の段階で別の関数挟まずに書き終えてて凄すぎてびっくりしてしまった。関数プログラミングっぽい書き方
nittoco: https://github.com/nittoco/leetcode/pull/14/files
rossy0213: https://github.com/rossy0213/leetcode/pull/10
Mike0121: https://github.com/Mike0121/LeetCode/pull/6#discussion_r1590279702
traverse_nodesに型ヒントを追加
"""
# 簡潔
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1



# phase1の直し, 型ヒントを追加, node == Noneをnode is Noneに
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        def traverse_nodes(node: Optional[TreeNode], depth: int) -> None:
            # node: the node you concentrate on
            # depth: the depth of the node you concentrate on
            nonlocal max_depth
            if node is None:
                return
            if max_depth < depth:
                max_depth = depth
            traverse_nodes(node.left, depth + 1)
            traverse_nodes(node.right, depth + 1)

        traverse_nodes(root, 1)
        return max_depth

# 一応再帰以外でも
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        stack = [(root, 1)] 
        while stack:
            current_node, depth_so_far = stack.pop()
            if current_node is None:
                continue
            if max_depth < depth_so_far:
                max_depth = depth_so_far
            stack.append((current_node.right, depth_so_far + 1))
            stack.append((current_node.left, depth_so_far + 1))

        return max_depth
