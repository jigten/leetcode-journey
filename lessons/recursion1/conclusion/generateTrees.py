from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root):
    if root != None:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)


def generateTrees(n: int) -> List[Optional[TreeNode]]:
    if n == 0:
        return []

    def helper(start, end):
        trees = []
        if start > end:
            trees.append(None)
            return trees

        for i in range(start, end + 1):
            left_trees = helper(start, i - 1)
            right_trees = helper(i + 1, end)
            for l in left_trees:
                for r in right_trees:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    trees.append(root)
        return trees

    return helper(1, n)


if __name__ == "__main__":
    trees = generateTrees(n=3)
    for i in range(len(trees)):
        preorder(trees[i])
        print()
