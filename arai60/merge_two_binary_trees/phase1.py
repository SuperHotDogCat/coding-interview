# 28分, merge方法に苦しんだ末にどうにか思いつく
# root1にroot2を統合するイメージ
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return
        elif root1 is None:
            root1 = TreeNode()
        elif root2 is None:
            root2 = TreeNode()
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
