class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def skip_duplicated_nodes(head: Optional[ListNode]) -> Optional[ListNode]:
            while head.next and head.val == head.next.val:
                head = head.next
            return head
        dummy_head = ListNode(-1)
        current_node = dummy_head
        while head:
            if head.next and head.val == head.next.val:
                head = skip_duplicated_nodes(head)
            else:
                current_node.next = ListNode(head.val)
                current_node = current_node.next
            head = head.next
        return dummy_head.next