class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def dfs(openN, closedN):
            if(openN == closedN == n):
                res.append("".join(stack))
            if(openN < n): #can only add as many open parentheses as there are n characters given
                stack.append("(")
                dfs(openN+1,closedN)
                stack.pop() #pops the open to get rid of it in case the next case does not use
            if(closedN < openN): #can only add closed parenthesis if there are more open parentheses
                stack.append(")")
                dfs(openN,closedN+1)
                stack.pop() #pops the closed in case the next case does not want to use it
        
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


            
        