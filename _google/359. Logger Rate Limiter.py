"""
Problem:
    Design a logger system that receives a stream of messages along with their timestamps.
    Each unique message should only be printed at most every 10 seconds.

    All messages will come in chronological order. Several messages may arrive at the same timestamp.

    Implement the Logger class.
"""


class Logger:
    def __init__(self):
        self.messages = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messages:
            self.messages[message] = timestamp
            return True

        if timestamp - self.messages[message] >= 10:
            self.messages[message] = timestamp
            return True

        return False
