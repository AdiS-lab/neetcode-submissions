

class Twitter:

    def __init__(self):
        self.posts = {}
        self.followers = {}
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.setdefault(userId, {})
        self.posts[userId][tweetId] = self.counter
        self.counter += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        twitter_posts = []

        if userId in self.followers:
            for fId in self.followers[userId].keys():
                if fId in self.posts:
                    for twitterId, place in self.posts[fId].items():
                        twitter_posts.append((twitterId, place))

        if userId in self.posts:
            for self_post, place in self.posts[userId].items():
                twitter_posts.append((self_post, place))
 
        sorted_posts = sorted(twitter_posts, key=lambda x: [-x[1], x[0]])

        res = [post_id for post_id, _ in sorted_posts]
        return res[0:10] if len(res) > 10 else res


    def follow(self, followerId: int, followeeId: int) -> None:

        self.followers.setdefault(followerId, {})
        self.followers[followerId][followeeId] = "arbitrary"

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followeeId in self.followers[followerId]:
            del self.followers[followerId][followeeId]