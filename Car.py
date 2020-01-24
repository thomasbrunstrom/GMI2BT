class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def read_odometer(self):
        print(f'Bilen har åkt {self.odometer_reading}km')
    
    def update_odometer(self, value):
        self.odometer_reading = value

    def get_descriptive_name(self):
        long_name = f'{str(self.year)} {self.make} {self.model}'
        return long_name.title()

class Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f'Bilen har ett {self.battery_size}-kWh batteri')
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = f'Bilen kommer ca {self.battery_size}km på '
        message += 'en full laddning'
        print(message)

class ElectricCar(Car):
    def __init(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    
