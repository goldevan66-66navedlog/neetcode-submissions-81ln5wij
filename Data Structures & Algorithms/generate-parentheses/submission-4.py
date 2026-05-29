class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def dfs(openN, closedN):
            if(openN == closedN == n):
                res.append("".join(stack))
            if(openN < n):
                stack.append("(")
                dfs(openN+1,closedN)
                stack.pop()
            if(closedN < openN):
                stack.append(")")
                dfs(openN,closedN+1)
                stack.pop()
        
        dfs(0,0)
        return res
        # res = set()

        # def dfs(n,cur):
        #     if(n == 0):
        #         res.add(cur)
        #         return

        #     # w = cur.copy()
        #     # cur = "(" + cur + ")"
        #     dfs(n-1,"("+cur+")")
        #     dfs(n-1,cur+"()")
        #     dfs(n-1,"()"+cur)
        
        # dfs(n,"")
        # return [p for p in res]


            
        