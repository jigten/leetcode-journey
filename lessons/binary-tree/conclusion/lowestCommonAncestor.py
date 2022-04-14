# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
    p_path, q_path = [], []

    def findPath(root, n, path):
        if not root:
            return None

        n_l = findPath(root.left, n, path)
        n_r = findPath(root.right, n, path)

        if root == n:
            path.append(root)
            return root

        if n_l or n_r:
            path.append(root)
            return root

    findPath(root, p, p_path)
    findPath(root, q, q_path)
    p_path.reverse()
    q_path.reverse()

    i = 0
    while i < len(p_path) and i < len(q_path):
        if p_path[i].val != q_path[i].val:
            break
        i += 1
    return p_path[i - 1]


if __name__ == "__main__":
    root = TreeNode(3)

    root.left = TreeNode(5)
    root.left.left = TreeNode(6)

    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    root.right = TreeNode(1)

    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    print(lowestCommonAncestor(root, root.left, root.right))
