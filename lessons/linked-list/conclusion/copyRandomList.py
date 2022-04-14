from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    last, n = head, 1
    while last.next:
        last = last.next
        n += 1

    if k % n == 0:
        return head

    middle = head
    for _ in range(n - k % n - 1):
        middle = middle.next

    new_head = middle.next
    last.next = head
    middle.next = None
    return new_head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    res = rotateRight(head, 2)
    while res:
        print("node: ", res.val)
        res = res.next
