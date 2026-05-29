class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # if(len(nums) == 0):
        #     return [[]]
        # perms = self.permute(nums[1:])
        # res = []
        # for p in perms:
        #     for i in range(len(p)+1):
        #         p_copy = p.copy()
        #         p_copy.insert(i,nums[0])
        #         res.append(p_copy)
        # return res
        perms = [[]]
        for n in nums:
            newperm = []
            for p in perms:
                for i in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(i,n)
                    newperm.append(p_copy)
            perms = newperm
        return perms

        # res = []
        # curr = []
        # def rotate(lst):
        #     if(len(lst)==1):
        #         res.append(curr.copy())
        #         return
        #     else:
        #         curr.append(lst[0])
        #         for i in range(len(lst)-1):
        #             curr.append(lst[i+1])
        #             lst
        #             rotate(i)
        #             curr.pop()
        # res = []

        # curr = []
        # def dfs(i, ns, rot):
        #     if(i >= len(ns) or rot >= len(ns) or len(curr) >= len(ns)):
        #         if(len(curr) == len(ns)):
        #             res.append(curr.copy())
        #         return
        #     else:
        #         curr.append(ns[i])
        #         dfs(i+1,ns,rot)
        #         print(curr)

        #         curr.pop()
        #         dfs(0,ns[i+1:]+ns[:i+1],rot+1)
        
        # # for i in range(0,len(nums)):
        # #     dfs(0,nums[i:]+nums[:i])
        # dfs(0,nums,0)

        # return res

                
        