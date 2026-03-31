# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, tree1, tree2) -> bool:
        if (tree1 is None and tree2 is None):
            return True
        if (tree1 and tree2 and tree1.val == tree2.val):
            return self.isSameTree(tree1.left, tree2.left) and self.isSameTree(tree1.right, tree2.right)
        else: return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (root is None):
            return False
        if (self.isSameTree(root, subRoot)):
            return True
        else: return(self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        