class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bstFromPreorder(self, preorder) -> TreeNode:
    if not preorder: return None

    root = TreeNode(preorder[0])
    i = 1
    while i < len(preorder):
        if preorder[i] < preorder[0]: i+= 1
        else: break

    root.left = self.bstFromPreorder(preorder[1:i])
    root.right = self.bstFromPreorder(preorder[i:])

    return root


