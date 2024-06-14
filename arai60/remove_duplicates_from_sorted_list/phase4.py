class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node:
            while node.next and node.val == node.next.val:
                node.next = node.next.next
            node = node.next
        return head

# 再帰version
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        def deleteDuplicatesNodes(node: Optional[ListNode]) -> None:
            # nodeより先の重複したノードを返す
            if node == None:
                return None
            if node.next and node.val == node.next.val:
                node.next = node.next.next
                return deleteDuplicatesNodes(node)
            elif node.next is None:
                return deleteDuplicatesNodes(None)
            else:
                return deleteDuplicatesNodes(node.next)
        deleteDuplicatesNodes(node)
        return head

