class Car:
    def __init__(self, model, color, speed):
        self.__model = model
        self.__color = color
        self.__speed = speed
    def drive(self):
        pass
    def printCar(self):
        print(f'모델: {self.__model}, 색깔: {self.__color}, 속도: {self.__speed}')
        
    def getModel(self): return self.__model
    def getColor(self): return self.__color
    def getSpeed(self): return self.__speed
    def getCar(self) : return self.__model, self.__color, self.__speed
    
    def setModel(self, model): self.__model = model
    def setColor(self, color): self.__color = color
    def setSpeed(self, speed): self.__speed = speed
    
    def setCar(self, model, color, speed): 
        self.__model = model,
        self.__color = color,
        self.__speed = speed
            
class NewCar(Car):
    def drive(self):
        self.setSpeed(100) 
    def upSpeed(self, value):
        newSpeed = self.getSpeed() + value
        self.setSpeed(newSpeed)
    def downSpeed(self, value):
        newSpeed = self.getSpeed() - value
        self.setSpeed(newSpeed)

my_Car = NewCar('iClickseo', 'white', 0)
my_Car.printCar()
my_Car.drive()
my_Car.upSpeed(10)
my_Car.downSpeed(10)
        
        