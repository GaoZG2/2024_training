class Car:
    """⼀次模拟汽⻋的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽⻋的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """返回格式规范的描述性名称"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """打印⼀个句⼦，指出汽⻋的⾏驶⾥程"""
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        """将⾥程表读数设置为给定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """让⾥程表读数增加给定的量"""
        self.odometer_reading += miles

class Battery:
    """⼀次模拟电动汽⻋电池的简单尝试"""
    def __init__(self, battery_size=40):
        """初始化电池的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印⼀条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        """打印⼀条消息，指出电池的续航⾥程"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

class ElectricCar(Car):
    """电动汽⻋的独特之处"""
    def __init__(self, make, model, year):
        """
        先初始化⽗类的属性，再初始化电动汽⻋特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()

electric_car = ElectricCar('nissan', 'leaf', 2024)
electric_car.battery.get_range()

electric_car.battery.upgrade_battery()
electric_car.battery.get_range()


