from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    def helper(node, minVal, maxVal):
        if not node:
            return True
        if node.val <= minVal or node.val >= maxVal:
            return False
        if (node.left and node.left.val >= node.val) or (
            node.right and node.right.val <= node.val
        ):
            return False
        return helper(node.left, minVal, node.val) and helper(
            node.right, node.val, maxVal
        )

    return helper(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    root1 = TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3))
    print(isValidBST(root1))
    root2 = TreeNode(
        val=5,
        left=TreeNode(val=1),
        right=TreeNode(4, left=TreeNode(3), right=TreeNode(6)),
    )
    print(isValidBST(root2))
    root3 = TreeNode(val=1, right=TreeNode(val=1))
    print(isValidBST(root3))
    root4 = TreeNode(val=1, left=TreeNode(val=-1))
    print(isValidBST(root4))
