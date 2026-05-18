class Twitter:

    def __init__(self):
        self.following = {}
        self.posts = {}
        self.time = 0  

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.posts[userId] = self.posts.get(userId,[]) + [[self.time,tweetId]]   

    def getNewsFeed(self, userId: int) -> List[int]:
        ps = list(self.posts.get(userId,[]))

        if(self.following.get(userId,None)):
            for f in self.following.get(userId):
                ps += self.posts[f]
        ps = [[-t[0],t[1]] for t in ps]
        heapq.heapify(ps)
        
        res = []
        while(len(res)<10 and ps):
            res += [heapq.heappop(ps)[1]]

        return res#[t[1] for t in ps[:10]]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if(self.following.get(followerId,None) == None):
            self.following[followerId] = set()
        if(followerId != followeeId):
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if(followerId != followeeId and followeeId in self.following[followerId]):
            self.following[followerId].remove(followeeId)
        
