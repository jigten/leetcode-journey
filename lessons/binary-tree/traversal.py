from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    def helper(root, res=[]):
        if not root:
            return

        helper(root.left, res)
        helper(root.right, res)
        res.append(root.val)
        return res

    return helper(root)


if __name__ == "__main__":
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print(preorderTraversal(root))
