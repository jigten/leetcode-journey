class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        current = self.head
        temp = Node(val)
        if index <= 0:
            temp.next = current
            self.head = temp
        else:
            for _ in range(index - 1):
                current = current.next
            temp.next = current.next
            current.next = temp
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return

        current = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.length -= 1


if __name__ == "__main__":
    obj = MyLinkedList()
    param_1 = obj.get(1)
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1, 2)
    obj.deleteAtIndex(2)
