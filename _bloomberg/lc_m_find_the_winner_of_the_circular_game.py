"""
1823. Find the Winner of the Circular Game
https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/

Problem:
    There are N number of friends, and K which is moving in circle. If K stops in some person after K steps, then
    that person leaves the game. And game continues till 1 person left.

Solution 1:
    - Creating an array of people and remove item when K stops.
    - Use normalized K value, because K might be larger than the number of people left.
"""


from collections import deque


# Time O(N^2) | Space O(N)
def findTheWinner(n: int, k: int) -> int:
    people = list(range(1, n + 1))
    index_of_person = 0

    while len(people) > 1:
        index_of_person = (index_of_person + k - 1) % len(people)
        people.pop(index_of_person)

    return people.pop()


# Time O(N) | Space O(N)
def findTheWinnerDeque(n: int, k: int) -> int:
    nums = deque(range(n))
    while len(nums) > 1:
        nums.rotate(1-k)
        nums.popleft()
    return nums[0] + 1