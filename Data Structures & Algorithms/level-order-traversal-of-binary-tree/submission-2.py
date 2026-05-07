# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = {}
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = {}
        def dfs(root,level):
            nonlocal res
            if(not root):
                return 0
            res[level] = res.get(level,[]) + [root.val]
            return dfs(root.left, level+1) + dfs(root.right,level+1)
        dfs(root,0)
        return [res[i] for i in res.keys()]
        