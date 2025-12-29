import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)    
        self.following = defaultdict(set) 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []

        self.following[userId].add(userId)

        for followee in self.following[userId]:
            if followee in self.tweets:
                for time, tweetId in self.tweets[followee][-10:]:
                    heapq.heappush(maxHeap, (-time, tweetId))

        res = []
        while maxHeap and len(res) < 10:
            _, tweetId = heapq.heappop(maxHeap)
            res.append(tweetId)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
