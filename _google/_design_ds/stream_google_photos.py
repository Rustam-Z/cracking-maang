"""
https://leetcode.com/discuss/interview-question/2072005/Google-or-Phone-Screening-or-Google-Photos-Client

Suppose you are uploading 10 Photos, The server can respond back in any order, such as 1,2,4,5,3,7,6,10,9,8.
Now at any given point of time we need to check what is the maximum photo number which has been uploaded continuously.

ack(1),
getMax()-> returns 1, because the maximum photo uploaded is 1
ack(2),
getMax()-> returns 2, because the maximum photo uploaded is 2
ack(4)
getMax()-> returns 2 only because 3 has not been recieved yet
ack(5)
getMax()-> returns 2 again because 3 has not been recieved yet
ack(3)
getMax()-> returns 5 because we recieved 3 and 4 and 5 also we recieved eralier.
"""


class AckConstraintTime:
    def __init__(self, n):
        self.photos = [False for i in range(n)]
        self.ptr = 0

    def ack(self, x):
        self.photos[x - 1] = True

    def getMax(self):
        while self.ptr < len(self.photos) and self.photos[self.ptr]:
            self.ptr += 1
        return self.ptr


class GetMaxConstraintTime:
    def __init__(self, n):
        self.photos = set()
        self.ptr = 1

    def ack(self, x):
        photos, ptr = self.photos, self.ptr
        self.photos.add(x)
        while ptr in photos:
            ptr += 1
        self.ptr = ptr

    def getMax(self):
        return self.ptr - 1
