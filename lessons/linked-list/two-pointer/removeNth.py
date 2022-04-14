from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if not head:
        return None

    pA = head
    for _ in range(n):
        pA = pA.next

    pB = head
    res = pB

    if not pA:
        pB = pB.next
        return pB

    while pA and pA.next:
        pB = pB.next
        pA = pA.next

    if not pB.next:
        return None

    if pB.next and not pB.next.next:
        pB.next = None
        return res

    if pB.next and pB.next.next:
        pB.next = pB.next.next
        return res


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)

    res = removeNthFromEnd(head, 2)
    while res:
        print(res.val)
        res = res.next
