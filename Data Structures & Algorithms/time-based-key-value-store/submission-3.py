class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # self.dic[key] += [[timestamp,value]]
        self.dic[key] = self.dic.get(key,[]) + [[timestamp,value]]

    def get(self, key: str, timestamp: int) -> str:
        lst = self.dic.get(key,None)
        if(lst == None):
            return ""
        l = 0
        r = len(lst)
        m = (l+r)//2
        print(lst)
        while(l < r):
            m = (l+r)//2
            if(lst[m][0] >= timestamp):
                r = m
                if(lst[m][0] == timestamp):
                    return lst[m][1]
            elif(lst[m][0] < timestamp):
                l = m+1
        print(l)
        return str(lst[l-1][1]) if lst[l-1][0] <= timestamp else ""

