class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or slow is None:
                return False

            slow = slow.next
            fast = fast.next.next

        return True