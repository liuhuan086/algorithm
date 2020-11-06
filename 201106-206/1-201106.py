# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            """
            cur是当前节点
            pre是上一个节点
            pre.next是pre.的下一个节点
            
            pre=cur 把当前节点赋值给上一个节点

            pre.next=pre 把上一个节点的值赋给上一个节点的下一个节点
            
            cur=pre.next 把上一个节点的下一个节点的值赋给当前节点
            """
            pre, pre.next, cur = cur, pre, pre.next

        return pre
