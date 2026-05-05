# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(not subRoot):
            return True
        elif(not root):
            return False
        elif(self.isSameTree(root,subRoot)):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
    def isSameTree(self, s, t):
        if(not s and not t):
            return True
        elif(not s or not t):
            return False
        else:
            return (s.val == t.val) and self.isSameTree(s.left,t.left) and self.isSameTree(s.right,t.right)
        