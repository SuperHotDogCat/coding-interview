class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current_head = dummy_head
        skip_number = None
        while head:
            if head.next and head.val != head.next.val and head.val != skip_number:
                current_head.next = ListNode(head.val)
                current_head = current_head.next
            elif head.next == None and head.val != skip_number:
                current_head.next = ListNode(head.val)
            skip_number = head.val
            head = head.next
        return dummy_head.next