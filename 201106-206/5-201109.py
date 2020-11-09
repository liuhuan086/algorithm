class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None

        while cur:
            tmp = cur.next
            cur.next = pre
            cur = tmp

        return cur

