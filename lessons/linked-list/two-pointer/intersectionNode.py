from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    if not headA or not headB:
        return None

    pA, pB = headA, headB
    while pA != pB:
        pA = headB if pA is None else pA.next
        pB = headA if pB is None else pB.next
    return pA.val


if __name__ == "__main__":
    head = ListNode(8)
    head.next = ListNode(4)
    head.next.next = ListNode(5)
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = head
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = head

    print(getIntersectionNode(headA, headB))
