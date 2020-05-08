from collections import deque
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.msg_set = set()
        self.msg_queue = deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        while self.msg_queue:
            msg, ts = self.msg_queue[0]
            print("timestamp, ts, message, msg:", timestamp, ts, message, msg)
            if timestamp - ts >= 10:
                self.msg_queue.popleft()
                self.msg_set.remove(msg)
            else:
                break

        if message not in self.msg_set:
            self.msg_set.add(message)
            self.msg_queue.append((message, timestamp))
            return True
        else:
            return False

# Your Logger object will be instantiated and called as such:
obj = Logger()

# ["Logger","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage"]
for (timestamp,message) in [[1,"foo"],[2,"bar"],[3,"foo"],[8,"bar"],[10,"foo"],[11,"foo"]]:
    param_1 = obj.shouldPrintMessage(timestamp,message)
    print(param_1)