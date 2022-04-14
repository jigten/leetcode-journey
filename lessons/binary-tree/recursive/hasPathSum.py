from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    def helper(root, targetSum):
        if not root:
            return False

        if not root.left and not root.right and root.val == targetSum:
            return True

        targetSum -= root.val

        return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)

    return helper(root, targetSum)


if __name__ == "__main__":
    root = TreeNode(5)

    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    # root.left.left.right = TreeNode(2)

    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    print(hasPathSum(root, 22))
