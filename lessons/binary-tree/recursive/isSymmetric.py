from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    def helper(left, right):
        if not left and not right:
            return True

        if not left and right or left and not right:
            return False

        if not left.left and right.right or left.right and not right.left:
            return False

        if left.val != right.val:
            return False

        return helper(left.left, right.right) and helper(left.right, right.left)

    return helper(root.left, root.right)


if __name__ == "__main__":
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.left.left = TreeNode(2)
    # root.left.right = TreeNode(3)

    root.right = TreeNode(2)
    root.right.left = TreeNode(2)
    # root.right.right = TreeNode(3)
    print(isSymmetric(root))
