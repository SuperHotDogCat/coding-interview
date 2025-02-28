# https://github.com/SuperHotDogCat/coding-interview/pull/43#discussion_r1958958113 
# このコードを買いている時どうも命名に気を配れていなかった。数字でノード1つを指定できるのでidという名前にしていたがTreeNodeの名前はvalなのでそこが違うために困惑させたコードになってしまっていた
# あとは変数を定義してから使うまでを離さないように

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_inorder_index = inorder.index(root_val)
        root.left = self.buildTree(preorder[1:1 + root_inorder_index], inorder[:root_inorder_index])
        root.right = self.buildTree(preorder[1 + root_inorder_index:], inorder[root_inorder_index + 1:])
        return root

# https://github.com/SuperHotDogCat/coding-interview/pull/43/files#r1958006329
# https://github.com/SuperHotDogCat/coding-interview/pull/43/files#r1957333097 コメント: 個人的にはどれくらい消費したかを返り値で返して欲しいですね<-消費したかを返す実装で自分は沼にハマってしまったのでpreorder_indexを返すように関数を変更して副作用を消すようにした
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        node_val_to_inorder_index = {val: i for i, val in enumerate(inorder)}

        def build_tree_helper(left: int, right: int, preorder_index: int):
            # preorder_indexは常に次探索すべきpreorderのindexを指すように制作
            if left > right:
                return None, preorder_index
            node = TreeNode(preorder[preorder_index])
            split_index = node_val_to_inorder_index[preorder[preorder_index]]
            preorder_index += 1
            node.left, preorder_index = build_tree_helper(left, split_index - 1, preorder_index)
            node.right, preorder_index = build_tree_helper(split_index + 1, right, preorder_index)
            return node, preorder_index
        return build_tree_helper(0, len(inorder) - 1, 0)[0]
