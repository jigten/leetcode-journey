from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    if not list1 and not list2:
        return None
    if not list1 and list2:
        return list2
    if list1 and not list2:
        return list1

    if list1.val <= list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    if list1.val > list2.val:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    merged = mergeTwoLists(list1, list2)
    while merged:
        print(merged.val)
        merged = merged.next
