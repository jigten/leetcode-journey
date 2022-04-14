from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return
    if root.val == val:
        return root
    return searchBST(root.left, val) or searchBST(root.right, val)


if __name__ == "__main__":
    root = TreeNode(4)

    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    root.right = TreeNode(7)

    ans = searchBST(root, 2)
    print(ans.val)
