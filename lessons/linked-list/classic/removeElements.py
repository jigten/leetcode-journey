from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if not head:
        return None

    curr = head
    prev = None

    while curr:
        if curr.val == val and not prev:
            head = head.next
            curr = head
            continue

        if curr.val == val and prev and curr.next:
            prev.next = curr.next
            curr = curr.next
            continue

        if curr.val == val and prev and not curr.next:
            prev.next = None
            curr = None
            continue

        prev = curr
        curr = curr.next

    return head


if __name__ == "__main__":
    head = ListNode(4)
    head.next = ListNode(1)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(4)
    res = removeElements(head, 4)
    while res:
        print(res.val)
        res = res.next
