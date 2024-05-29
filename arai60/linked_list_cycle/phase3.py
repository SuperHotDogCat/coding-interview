class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set([])
        node = head
        while node:
            if node in seen:
                return True
            seen.add(node)
            node = node.next
        return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's cycle-finding algorithm
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False