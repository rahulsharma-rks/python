import datetime
now = datetime.datetime.now()
class car():
    base_price = 100000 #Class Variable
    def __init__(self,windows,doors,power):
        self.windows = windows
        self.doors = doors
        self.power = power
    
    def base(self):
        print("Base Price is {}".format(self.base_price))
    
    @classmethod
    def revise_base_price(cls,inflation):
        cls.base_price = cls.base_price + cls.base_price * inflation

    @staticmethod
    def check_year(year):
        if now.year == 2021:
            return True
        else:
            return False


car.revise_base_price(0.10)

#car1 = car(4,5,1000)
#print(car1.base_price)
print(car.base_price)

print(car.check_year(2021))