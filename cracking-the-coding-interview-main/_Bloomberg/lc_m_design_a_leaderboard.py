"""1244. Design A Leaderboard
https://leetcode.ca/all/1244.html

Problem:
    Design a Leaderboard class, which has 3 functions:
    - addScore(playerId, score): Update the leaderboard by adding score to the given player's score.
      If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
    - top(K): Return the score sum of the top K players.
    - reset(playerId): Reset the score of the player with the given id to 0.
      It is guaranteed that the player was added to the leaderboard before calling this function.

Constraints and questions:
    - Initially, the leaderboard is empty.
    - How many function call we will have for each method?

Solution:
    - Heap data structure
"""
import collections
import heapq


class Leaderboard:
    def __init__(self):
        self.scores = collections.defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score  # O(1)

    def top(self, k: int) -> int:
        return sum(heapq.nlargest(k, self.scores.values()))  # O(N*logK), as we will have only K stages

    def reset(self, playerId: int) -> None:
        del self.scores[playerId]  # O(1)
