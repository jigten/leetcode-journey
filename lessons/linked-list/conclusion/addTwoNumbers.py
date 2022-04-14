from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if not l1:
        return l2

    if not l2:
        return l1

    l1_p, l2_p, prev, carry = l1, l2, None, 0
    while l1_p and l2_p:
        prev = l1_p
        sum_val = l1_p.val + l2_p.val + carry
        if sum_val > 9:
            l1_p.val = sum_val - 10
            carry = 1
            l1_p = l1_p.next
            l2_p = l2_p.next
        else:
            carry = 0
            l1_p.val = sum_val
            l1_p = l1_p.next
            l2_p = l2_p.next

    if l2_p:
        prev.next = l2_p
        l1_p = prev.next

    if l1_p:
        while l1_p.next:
            sum_val = l1_p.val + carry
            if sum_val > 9:
                l1_p.val = sum_val - 10
                carry = 1
                l1_p = l1_p.next
            else:
                carry = 0
                l1_p.val = sum_val
                l1_p = l1_p.next

    if carry and l1_p:
        sum_val = l1_p.val + carry
        if sum_val > 9:
            l1_p.val = sum_val - 10
            l1_p.next = ListNode(carry)
            l1_p = l1_p.next
        else:
            carry = 0
            l1_p.val = sum_val

    if carry and not l1_p:
        prev.next = ListNode(carry)

    return l1


if __name__ == "__main__":
    list1 = ListNode(9)
    list1.next = ListNode(1)
    list1.next.next = ListNode(6)
    # list1.next.next.next = ListNode(9)
    list2 = ListNode(0)
    # list2.next = ListNode(9)
    # list2.next.next = ListNode(9)
    addTwoNumbers(list1, list2)
    while list1:
        print(list1.val)
        list1 = list1.next
