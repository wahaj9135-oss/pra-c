class govt:
    def __init__(self, car_name):
        self.car_name = car_name
class car(govt):
    def __init__(self, car_name, model):
        super().__init__(car_name)
        self.model = model
    def display(self):
        print("Car Name:", self.car_name)
        print("Model:", self.model)
car1 = car("Toyota", "Camry")
car1.display()