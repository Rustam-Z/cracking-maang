"""
1845. Seat Reservation Manager
https://leetcode.com/problems/seat-reservation-manager/

Design a system that manages the reservation state of n seats that are numbered from 1 to n.

Constraints:
    For each call to reserve, it is guaranteed that there will be at least one unreserved seat.
    For each call to unreserve, it is guaranteed that seatNumber will be reserved.

O(logN * OP) time, where OP is number of operations, logN is needed for push and pop
O(N) space
"""

import heapq


class SeatManager:
    def __init__(self, n: int):
        self.free_seats = [i for i in range(1, n + 1)]

    def reserve(self) -> int:
        return heapq.heappop(self.free_seats)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.free_seats, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
