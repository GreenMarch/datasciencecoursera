import time
import threading
from collections import deque


class RequestTimestamps(object):

    # lock is for concurrency in a multi threaded system
    # 100 req/min translates to requests = 100 and windowTimeInSec = 60
    def __init__(self, requests, windowTimeInSec):
        self.timestamps = deque()
        self.lock = threading.Lock()
        self.requests = requests
        self.windowTimeInSec = windowTimeInSec

    # eviction of timestamps older than the window time
    def evictOlderTimestamps(self, currentTimestamp):
        while len(self.timestamps) != 0 and (currentTimestamp -
                                             self.timestamps[0] > self.windowTimeInSec):
            self.timestamps.popleft()


class SlidingWindowLogsRateLimiter(object):

    def __init__(self):
        self.lock = threading.Lock()
        self.ratelimiterMap = {}

    # Default of 100 req/minute
    # Add a new user with a request rate
    def addUser(self, userId, requests=100, windowTimeInSec=60):
        # hold lock to add in the user-metadata map
        with self.lock:
            if userId in self.ratelimiterMap:
                raise Exception("User already present")
            self.ratelimiterMap[userId] = RequestTimestamps(requests, windowTimeInSec)

    # Remove a user from the ratelimiter
    def removeUser(self, userId):
        with self.lock:
            if userId in self.ratelimiterMap:
                del self.ratelimiterMap[userId]

    # gives current time epoch in seconds
    @classmethod
    def getCurrentTimestampInSec(cls):
        return int(round(time.time()))

    # Checks if the service call should be allowed or not
    def shouldAllowServiceCall(self, userId):
        with self.lock:
            if userId not in self.ratelimiterMap:
                raise Exception("User is not present. Please white list and register the user for service")
        userTimestamps = self.ratelimiterMap[userId]
        with userTimestamps.lock:
            currentTimestamp = self.getCurrentTimestampInSec()
            # remove all the existing older timestamps
            userTimestamps.evictOlderTimestamps(currentTimestamp)
            userTimestamps.timestamps.append(currentTimestamp)
            if len(userTimestamps.timestamps) > userTimestamps.requests:
                return False
            return True

obj = SlidingWindowLogsRateLimiter()

# ["Logger","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage"]
for (timestamp,message) in [[1,"foo"],[2,"bar"],[3,"foo"],[8,"bar"],[10,"foo"],[11,"foo"]]:
    param_1 = obj.shouldAllowServiceCall(1,message)
    print(param_1)