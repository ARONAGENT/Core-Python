class stocks:
    def __init__(self,stock,price):
        self.stock=stock
        self.price=price
    
    def stockava(self,name):
        print(f'Mobile name     :{name}')
        print(f'Available Stock :{self.stock}')
        print(f'Their price     :{self.price}')
    
    def __add__(self,s):
        stock=self.stock+s.stock
        price=self.price+s.price
        print(f'total available stocks :{stock}')
        print(f'total price            :{price}')
    
print('--------------vivo stock----------------')
vivo=stocks(20,350000)
vivo.stockava('vivo')
print('--------------Realme stock----------------')
realme=stocks(23,475000)
realme.stockava('realme')
print("--------------Total stock-----------------")
total=vivo+realme