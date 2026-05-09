# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root,maxS):
            nonlocal res
            if not root:
                return None
            if(root.val >= maxS):
                res += 1
                maxS = root.val
            dfs(root.left, maxS)
            dfs(root.right, maxS)
            # else:

            #     dfs(root.left, maxS)
            #     dfs(root.right, maxS)
        
        dfs(root, float("-infinity"))
        return res
        