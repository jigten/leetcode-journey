from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    if not list1 and list2:
        return list2

    l1_p, l2_p, prev = list1, list2, None

    while l1_p and l2_p:
        if l1_p.val <= l2_p.val:
            if l1_p.next and l1_p.next.val < l2_p.val:
                l1_p = l1_p.next
                continue
            temp1 = l1_p.next
            l1_p.next = l2_p
            temp2 = l2_p.next
            l2_p.next = temp1
            prev = l2_p
            l2_p = temp2
            l1_p = l1_p.next.next
        else:
            if prev:
                temp1 = prev.next
                prev.next = l2_p
                temp2 = l2_p.next
                l2_p.next = temp1
                prev = prev.next
                l2_p = temp2
            else:
                dummy = ListNode(l2_p.val)
                dummy.next = l1_p
                list1 = dummy
                prev = dummy
                l2_p = l2_p.next
    if l1_p and prev:
        prev.next = l1_p
    if l2_p and prev:
        prev.next = l2_p
    return list1


if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(3)
    # list1.next.next = ListNode(4)
    list2 = ListNode(5)
    list2.next = ListNode(7)
    # list2.next.next = ListNode(4)
    mergeTwoLists(list1, list2)
    while list1:
        print(list1.val)
        list1 = list1.next
