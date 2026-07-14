class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {i[0]:[] for i in tickets}
        
        tickets.sort()
        for d,a, in tickets:
            adj[d].append(a)
        
        lst = ["JFK"]
        def dfs(n):
            if(len(lst) == len(tickets)+1):
                return True
            if n not in adj:
                return False
            temp = list(adj[n])
            for i, d in enumerate(temp):
                adj[n].pop(i)
                lst.append(d)
                if(dfs(d)):
                    return True
                adj[n].insert(i,d)
                lst.pop()
            return False
        dfs("JFK")
        return lst