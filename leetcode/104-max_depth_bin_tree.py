class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: TreeNode) -> int:
    def dept_find(node, cont):
        if not node: return cont

        return max(dept_find(node.left, cont+1), dept_find(node.right, cont+1))

    return dept_find(root, 0)



