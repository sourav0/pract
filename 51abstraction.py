from abc import abstractmethod
from abc import ABC
class vehicle(ABC):
    @abstractmethod
    def getnoofwheels(self):
        pass
class bus(vehicle):
    def getnoofwheels(self):
        print("no of wheels in bus 6")
class bike(vehicle):
    def getnoofwheels(self):
        print("no of wheels of a bike 2")
class car(vehicle):
    def getnoofwheels(self):
        print("no of wheels in car 4")
obj=bus()
obj.getnoofwheels()
ob=bike()
ob.getnoofwheels()
ob1=car()
ob1.getnoofwheels()
