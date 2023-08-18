import heapq
from typing import List


def canAttendAllMeetings(intervals):
    """
    https://leetcode.com/problems/meeting-rooms/

    Problem:
        Given an array of meeting time intervals where intervals[i] = [starti, endi],
        determine if a person could attend all meetings.
    """
    intervals.sort(key=lambda i: i[0])

    for i in range(1, len(intervals)):
        i1 = intervals[i - 1]
        i2 = intervals[i]

        if i1[1] > i2[0]:
            return False

    return True


def minMeetingRooms2(intervals: List[List[int]]) -> int:
    """
    https://leetcode.com/problems/meeting-rooms-ii/

    Problem:
        Given an array of meeting time intervals where intervals[i] = [starti, endi],
        return the minimum number of conference rooms required.
    """
    def brute_force(intervals):
        """
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        rooms = []

        for interval in intervals:
            if not rooms:
                rooms.append(interval)
                continue

            for room in rooms:
                if interval[0] >= room[1]:
                    room[1] = interval[1]
                    break
            else:
                rooms.append(interval)

        return len(rooms)

    def optimized(intervals):
        """
        Algorithm:
            - Sort the start and end times separately.
            - Iterate through the start times.
            - If the start time is less than the end time, increment the number of rooms.
            - Else, increment the end time index.

        Time complexity: O(nlogn)
        Space complexity: O(n)
        """
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])

        rooms = 0
        end_idx = 0

        for start in starts:
            if start < ends[end_idx]:
                rooms += 1
            else:
                end_idx += 1

        return rooms

    return optimized(intervals)


def hospitalMostEnteredRoom(N: int, patients: list) -> int:
    """
    https://leetcode.com/discuss/interview-question/2072047/Google-or-Onsite-or-Banglore-or-May-2022-or-Patient-Queue
    There are N rooms, find the room which has been entered by most patients.
    Only 1 patient can enter a room at a time.

    N = number of rooms
    patients: list of patients
        patient-1 = {start: 1, duration: 8}
        patient-2 = {start: 1, duration: 2}
        patient-3 = {start: 6, duration: 4}

    ROOM 0: 1 -> 9
    ROOM 1: 1 -> 3, 6 -> 10
    """

    def take_available_room(rooms) -> int:
        pass

    def get_room_with_most_patients(rooms) -> int:
        pass

    # Sort patients by their start time
    patients.sort(key=lambda x: x['start'])

    # Initialize a priority queue (min-heap) to keep track of room end times
    rooms = {i: [0, 0] for i in range(N)}  # Room index: end time, patient count

    # Iterate through each patient and allocate rooms
    for patient in patients:
        start_time = patient['start']
        duration = patient['duration']

        # Find available room, based on earliest end time in rooms. Use min-heap.
        room_index = take_available_room(rooms)

        # Update the room's end time
        rooms[room_index][0] = start_time + duration
        rooms[room_index][1] += 1

    # Find the room with the most patients
    room_index = get_room_with_most_patients(rooms)
    return room_index


if __name__ == "__main__":
    assert minMeetingRooms2([[0, 30], [5, 10], [15, 20]]) == 2
    assert minMeetingRooms2([[7, 10], [2, 4]]) == 1
    assert minMeetingRooms2([[13, 15], [1, 13]]) == 1
    assert minMeetingRooms2([[9, 10], [4, 9], [4, 17]]) == 2
    assert minMeetingRooms2([[2, 11], [6, 16], [11, 16]]) == 2

    assert hospitalMostEnteredRoom(
        2,
        [
            {"start": 1, "duration": 8},
            {"start": 1, "duration": 2},
            {"start": 6, "duration": 4}
        ]
    ) == 1
