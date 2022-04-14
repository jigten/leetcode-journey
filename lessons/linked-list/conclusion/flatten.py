from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return

    curr = head

    return


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.child = Node(7)
    head.next.next.child.next = Node(8)
    head.next.next.child.next.next = Node(9)
    head.next.next.child.next.next.next = Node(10)

    head.next.next.child.next.child = Node(11)
    head.next.next.child.next.child.next = Node(12)
    print(flatten(head))
