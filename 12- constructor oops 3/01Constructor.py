#A constructor in Python, defined by the __init__ method, is automatically called when an object of a class is created. 
# It initializes the object's attributes with the values provided during creation.
class laptops:
    def __init__(self):
        self.lpnm=None
        self.lprice=None
    def showNameandPrice(self,lpnm,lprice):
        print(f'laptop name is {lpnm} and price is {lprice}')

obj=laptops()
obj.showNameandPrice('victus','68999')

#Or
class laptop:
    def __init__(self,lpnm,lprice):
        self.lpnm=lpnm
        self.lprice=lprice
    
    def showdetails(self):
        print(f'laptop name is {self.lpnm} and price is {self.lprice}')

obj1=laptop('dell','85000')
obj1.showdetails()

