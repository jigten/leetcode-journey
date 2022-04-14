from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return
    queue = deque([root])
    res = []
    while queue:
        level = []
        for _ in range(len(queue)):
            curr_node = queue.popleft()
            level.append(curr_node.val)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        res.append(level)
    return res


if __name__ == "__main__":
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print(levelOrder(root))
