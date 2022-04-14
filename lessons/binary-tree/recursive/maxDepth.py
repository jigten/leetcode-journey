from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    ans = 1

    def helper(root, depth=1):
        if not root:
            return 0
        nonlocal ans
        if not root.left and not root.right:
            ans = max(ans, depth)

        helper(root.left, depth + 1)
        helper(root.right, depth + 1)

        return ans

    return helper(root)


def maxDepthBottomUp(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    leftDepth = maxDepthBottomUp(root.left)
    rightDepth = maxDepthBottomUp(root.right)

    if not root.right and not root.left:
        return max(leftDepth, rightDepth) + 1

    return max(leftDepth, rightDepth) + 1


if __name__ == "__main__":
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    root.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.left.left = TreeNode(7)
    print(maxDepthBottomUp(root))
