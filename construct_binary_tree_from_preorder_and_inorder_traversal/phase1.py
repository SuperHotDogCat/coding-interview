# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# preorder, inorderを受け取るとその部分木を生成する関数を組むように制作した

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        
        node = TreeNode()
        root_id = preorder[0]
        index = inorder.index(root_id)
        node.val = root_id
        left_inorder = inorder[:index]
        left_preorder = preorder[1:1+len(left_inorder)]
        right_inorder = inorder[index + 1:]
        right_preorder = preorder[1+len(left_inorder):]
        node.left = self.buildTree(left_preorder, left_inorder)
        node.right = self.buildTree(right_preorder, right_inorder)

        return node
