# 副作用はあるが, sliceとかコピーをなしにして自分がギリギリ思いつきそうな解答を書いた

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_index = -1
        node_val_to_inorder_index = {val: i for i, val in enumerate(inorder)}
        def build_tree_helper(left: int, right: int):
            if left > right:
                return
            nonlocal preorder_index
            preorder_index += 1
            split_index = node_val_to_inorder_index[preorder[preorder_index]]
            node = TreeNode(preorder[preorder_index])
            node.left = build_tree_helper(left, split_index - 1)
            node.right = build_tree_helper(split_index + 1, right)
            return node
        return build_tree_helper(0, len(inorder) - 1)
