from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return
    if not head.next:
        return head

    temp = head.next.next
    head.next.next, head = head, head.next
    head.next.next = swapPairs(temp)
    return head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    res = swapPairs(head)
    while res:
        print(res.val)
        res = res.next
