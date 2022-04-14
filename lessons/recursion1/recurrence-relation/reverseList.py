from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    def helper(node, prev=None):
        if not node:
            return prev
        temp = node.next
        node.next = prev
        return helper(temp, node)

    return helper(head)


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    res = reverseList(head)
    while res:
        print(res.val)
        res = res.next
