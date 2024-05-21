class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = head
        while head:
            while head.next and head.val == head.next.val:
                # recconect listnodes in order to delete duplicates
                head.next = head.next.next
            head = head.next
        return dummy_head