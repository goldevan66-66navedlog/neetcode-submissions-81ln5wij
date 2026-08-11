class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = {i:float("inf") for i in range(0,amount+1)}
        res[0] = 0

        for k in res.keys():
            for c in coins:
                if(k-c in res):
                    res[k] = min(1+res[k-c],res[k])
        
        return res[amount] if res[amount] != float("inf") else -1