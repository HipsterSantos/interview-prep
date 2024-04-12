class Engine:
    def __init__(self,horsepower):
        self.horsepower = horsepower
    def start(self):
        print("Enginer has started with Horse power is ", self.horsepower)
    def stop(self): print("enginne has been stopped")


class Car:
    def __init__(self,make,model,engine):
        self.make = make
        self.model = model
        self.engine = engine

    def start(self):
        self.engine.start()
    def stop(self):
        self.engine.stop()

engine = Engine(horsepower=200)

# Creating a Car instance with the Engine instance
my_car = Car(make="Toyota", model="Camry", engine=engine)

# Starting and stopping the car
my_car.start()
my_car.stop()