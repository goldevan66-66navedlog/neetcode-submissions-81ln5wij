# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        ops = 0
        q = deque()
        q.append(root)

        def count(nums):
            count = 0
            sorted_nums = sorted(nums)
            idx = {n:i for i,n in enumerate(nums)}

            for i in range(len(nums)):
                if(nums[i] != sorted_nums[i]):
                    count += 1

                    j = idx[sorted_nums[i]]

                    nums[i], nums[j] = nums[j], nums[i]

                    idx[nums[j]] = j
            
            return count

        while q:
            length = len(q)
            vals = []
            for i in range(length):
                r = q.popleft()
                vals.append(r.val)
                if(r.left):
                    q.append(r.left)
                if(r.right):
                    q.append(r.right)
            
            ops += count(vals)

            
        return ops