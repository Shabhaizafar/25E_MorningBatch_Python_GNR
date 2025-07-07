from abc import ABC,abstractmethod

# Abstract Class
class Vehicle(ABC) : 

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle) : 
    def start(self):
        print("Car Start")

    # def stop(self):
    #     print("Car Stop")



c1 = Car()
c1.start()
c1.stop()