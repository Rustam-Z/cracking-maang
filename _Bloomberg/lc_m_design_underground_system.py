"""
https://leetcode.com/problems/design-underground-system/submissions/

Problem:
    An underground railway system is keeping track of customer travel times between different stations.
    They are using this data to calculate the average time it takes to travel from one station to another.
    Design the system with checkIn, checkOut, and getAverageTime functions.

Constraints:
    - A customer can only be checked into one place at a time.
    - There is at least 1 customer to calculate the average.
    - Time format is given in integers.
    - Before checking out, the customer checks in.

Solution:
    - Use 2 hash tables
        - 1st for saving checkins
            {
                "id1": (startStation, startTime),
                ...
            }
        - 2nd for creating a trip time
            {
                (startStation, endStation): [overallTime, numberOfUsers],
                (startStation2, endStation2): [overallTime, numberOfUsers],
            }
    - So the main logic will be written in checkOut.
        - First we get the users startStation and startTime from 1st dict
        - We need to check if (startStation, endStation) is in dict. If it is inside dict then we increment values.
          Otherwise, we create a new key.
"""


class UndergroundSystem:

    def __init__(self):
        self.checkins = {}  # To save only the station, time for given user
        self.tripTime = {}  # To save start & end station == time & quantity

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # Most of the work will be done here
        startStationName, startTime = self.checkins[id]
        travelTime = t - startTime

        if (startStationName, stationName) in self.tripTime:
            self.tripTime[(startStationName, stationName)][0] += travelTime
            self.tripTime[(startStationName, stationName)][1] += 1
        else:
            self.tripTime[(startStationName, stationName)] = [travelTime, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        overalTravelTime, quantity = self.tripTime[(startStation, endStation)]
        return overalTravelTime / quantity

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
