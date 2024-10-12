"""
Intuition:
    -> Need to store the tweet info
    -> Need to maintain timestamp for ordering of tweets
    -> Above two can be maintained as {list}
    -> For maintaining following info, we maintain a {set}// to avoid adding userinfo
    -> time which denotes the timestamp when the tweet is being posted
KEYPOINTS:
    Main logic impl is in News Feed:
	•	For a user’s news feed, we need to fetch tweets from both the user and the users they follow, but only the 10 most recent tweets.
	•	To efficiently fetch and sort these tweets, use a max-heap (priority queue) that always gives the most recent tweet first.
	•	The heap allows us to keep track of the latest tweets from the user and their followees, and extract the 10 most recent ones.

Post Tweet: Append the tweet with the current timestamp to the user’s list.
Get News Feed:
	•	Gather tweets from the user and their followees.
	•	Use a max-heap to collect and sort the most recent tweets.
	•	Return the top 10 tweets.
Follow: Add the followee to the follower’s following set.
Unfollow: Remove the followee from the follower’s following set.

TC:
postTweet(): O(1) – Constant time to post a tweet.
getNewsFeed(): O(k log f) – k = 10 tweets, f users (self + followees).
follow() and unfollow(): O(1) – Constant time for adding/removing from a set.


"""
import heapq
from collections import defaultdict
from typing import List

class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)  # {userId: [(timestamp, tweetId)]}
        self.following = defaultdict(set)  # {userId: {followeeIds}}
        self.time = 0  # Global timestamp to maintain the order of tweets

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Add the tweet with a timestamp
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Get the list of users whose tweets we need to fetch (self + followees)
        users_to_fetch = [userId] + list(self.following[userId])

        # Max-heap to store the most recent tweets
        maxheap = []
        feed = []

        # Add the last tweet of each user to the heap
        for user in users_to_fetch:
            if user in self.tweets and len(self.tweets[user]) > 0:
                last_tweet_idx = len(self.tweets[user]) - 1  # Last tweet index
                timestamp, tweetId = self.tweets[user][last_tweet_idx]
                heapq.heappush(maxheap, (-timestamp, tweetId, user, last_tweet_idx))

        # Extract the top 10 most recent tweets
        while maxheap and len(feed) < 10:
            latest_ts, tweetId, user, last_tweet_idx = heapq.heappop(maxheap)
            feed.append(tweetId)

            # If the user has more tweets, add the next recent tweet
            if last_tweet_idx > 0:
                next_tweet_idx = last_tweet_idx - 1
                timestamp, tweetId = self.tweets[user][next_tweet_idx]
                heapq.heappush(maxheap, (-timestamp, tweetId, user, next_tweet_idx))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add followee to the follower's following list
        if followerId != followeeId:  # Users can't follow themselves
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove followee from follower's following list if exists
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
