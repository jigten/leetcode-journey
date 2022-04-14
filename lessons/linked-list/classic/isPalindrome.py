from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: Optional[ListNode]) -> bool:
    if not head:
        return True

    f_p, s_p, i = head, head, 0

    while f_p and f_p.next:
        f_p = f_p.next.next
        s_p = s_p.next
        i += 0

    if f_p:
        s_p = s_p.next

    prev, curr = None, s_p
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    while prev:
        if prev.val == head.val:
            prev = prev.next
            head = head.next
            continue
        return False
    return True


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(2)
    # head.next.next.next = ListNode(1)
    # head.next.next.next.next = ListNode(1)
    print(isPalindrome(head))
