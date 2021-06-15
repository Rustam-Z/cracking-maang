class ParkingSystem:
    big, medium, small = 0, 0, 0

    def __init__(self, big: int, medium: int, small: int):
        __class__.big = big          # 1 
        __class__.medium = medium    # 2
        __class__.small = small      # 3
        

    def addCar(self, carType: int) -> bool:
        # We must park with the particular carType
        # types = [1, 2, 3]
        # size = [__class__.big, __class__.medium, __class__.small]
        if carType == 1 and __class__.big == 0 or carType == 2 and __class__.medium == 0 or carType == 3 and __class__.small == 0:
            return False
        if carType == 1: 
            __class__.big -= 1
        if carType == 2:
            __class__.medium -= 1
        if carType == 3:
            __class__.small -= 1
        return True

# Your ParkingSystem object will be instantiated and called as such:
obj = ParkingSystem(1, 1, 1)
param_1 = obj.addCar(1)
print(param_1)