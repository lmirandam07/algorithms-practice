# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumEvenGrandparent(root: TreeNode) -> int:
    if not root: return 0

    def helper(node, grand_p):
        if not node: return 0

        total = 0

        if grand_p:
            if node.left: total += node.left.val
            if node.right: total += node.right.val

        grand_p = True if node.val % 2 == 0 else False

        return total + helper(node.left, grand_p) + helper(node.right, grand_p)

    grand_p = True if root.val % 2 == 0 else False

    return helper(root.left, grand_p) + helper(root.right, grand_p)
