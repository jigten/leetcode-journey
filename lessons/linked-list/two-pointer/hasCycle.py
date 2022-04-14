from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        if not fast:
            return False
        slow = slow.next
        if fast == slow:
            return True
    return False


def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow2 = head
            while slow != slow2:
                slow = slow.next
                slow2 = slow2.next
            return slow


if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    print(detectCycle(head))
