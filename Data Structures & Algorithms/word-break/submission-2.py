class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if((i+len(w)) <= len(s) and s[i:i+len(w)] == w):
                    dp[i] = dp[i+len(w)]
                if(dp[i]):
                    break
        return dp[0]

        # words = {}

        # for w in wordDict:
        #     words[w[0]] = words.get(w[0],[]) + [w]
        
        # def dfs(i):
        #     if(i >= len(s)):
        #         return True
        #     l1 = s[i]
        #     if(l1 not in words):
        #         return False
        #     lw = words[l1]
        #     for w in lw:
        #         print(w)
        #         lenw = len(w)
        #         if(s[i:i+lenw] == w):
        #              return dfs(i+lenw)
        #         else:
        #             continue
        #     return False
        # return dfs(0)
