"""
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
"""


class BruteForce:
    """
    Algorithm:
        - Create a dictionary that will have the snapshots as keys and the array as values.

    Time complexity: O(1) for set, O(1) for snap, O(1) for get
    Space complexity: O(n) because we store all the snapshots
        TODO next solution: What if we can only snapshot the keys that change.
    """

    def __init__(self, length: int):
        self.snap_id = 0
        self.current = [0] * length
        self.snapshots = dict()

    def set(self, index: int, val: int) -> None:
        self.current[index] = val

    def snap(self) -> int:
        # TAKE SNAPSHOT
        self.snapshots[self.snap_id] = self.current.copy()
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshots[snap_id][index]


class SnapshotArray:
    """
    Algorithm:
        - set() will add the value to the array at the given index.
        - We will modify get() to use binary search to find the value at the given index at the given snapshot.
    """

    def __init__(self, length: int):
        self.data = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.data[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snapshots = self.data[index]
        left, right = 0, len(snapshots) - 1

        while left <= right:
            mid = (left + right) // 2

            if snapshots[mid][0] == snap_id:
                return snapshots[mid][1]
            elif snapshots[mid][0] < snap_id:
                left = mid + 1
            else:
                right = mid - 1

        return snapshots[right][1] # if right >= 0 else 0


if __name__ == '__main__':
    snapshot = BruteForce(1)
    snapshot.snap() # 0
    snapshot.snap() # 1
    snapshot.set(0, 4)
    snapshot.snap() # 2
    snapshot.get(0, 1)
    snapshot.set(0, 12)
    snapshot.get(0, 1)
    snapshot.snap() # 3
    snapshot.get(0, 3)
