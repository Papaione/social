print("__________________________________________________________________")
print("|  PERSON \U0001F464 |   RATING \u2764 |  FRIENDS \U0001F465|    POSTS \U0001F6A9| COMMENTS \U0001F4AC|")
class User:
    def __init__(self, nickname, rating, friends, posts, comments):
        self.nickname = nickname
        self.rating   = rating
        self.friends  = friends
        self.posts    = posts
        self.comments = comments

    def __str__(self): 
        return f"|{self.nickname:>12}|{self.rating:12}|{self.friends:>12}|{self.posts:12}|{self.comments:12}|"

    def addl(self):
        self.rating += 1

    def dell(self):
        if self.ratingp():
            self.rating -= 1
            while self.ratingn():
                self.rating = self.rating + 1

    def ratingp(self):
        return self.rating >= 0

    def ratingn(self):
        return self.rating <= -1

    def addf(self):
        self.friends += 1

    def delf(self):
        if self.friendsp():
            self.friends -= 1
            while self.friendsn():
                self.friends = self.friends + 1

    def friendsp(self):
        return self.friends >= 0

    def friendsn(self):
        return self.friends <= -1

    def addp(self):
        self.posts += 1

    def delp(self):
        if self.postsp():
            self.posts -= 1
            while self.postsn():
                self.posts = self.posts + 1

    def postsp(self):
        return self.posts >= 0

    def postsn(self):
        return self.posts <= -1

    def addc(self):
        self.comments += 1

    def delc(self):
        if self.commentsp():
            self.comments -= 1
            while self.commentsn():
                self.comments = self.comments + 1

    def commentsp(self):
        return self.comments >= 0

    def commentsn(self):
        return self.comments <= -1

#########################################
users = []
users.append(  User("Marry", 4.0, 234,  13, 35) )
users.append(  User("John",  3.5,  23,  43, 12) )
users.append(  User("Kate",  0,    92,  24, 32) )

users[1].addl()
users[2].dell()
users[1].addf()
users[2].delf()
users[1].addp()
users[2].delp()
users[1].addc()
users[2].delc()

for u in users:
    print( u )

