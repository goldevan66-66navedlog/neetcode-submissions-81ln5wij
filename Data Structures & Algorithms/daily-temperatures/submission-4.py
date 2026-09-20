class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i,t in enumerate(temperatures):
            if not stack:
                stack.append(i)
            else:
                for j in range(len(stack)):
                    if(temperatures[stack[-1]] < t):
                        index = stack.pop()
                        res[index] = i-index
                    else:
                        break
                stack.append(i)
        
        return res
