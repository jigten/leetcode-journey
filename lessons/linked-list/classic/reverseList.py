from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    curr, prev = head, None
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    return prev


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    rev = reverseList(head)
    while rev:
        print(rev.val)
        rev = rev.next
