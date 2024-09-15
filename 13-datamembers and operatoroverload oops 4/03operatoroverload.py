class Stocks:
    def __init__(self, stock, price):
        self.stock = stock
        self.price = price
    
    def stockava(self, name):
        print(f'Mobile name     : {name}')
        print(f'Available Stock : {self.stock}')
        print(f'Their price     : {self.price}')
    
    def __add__(self, other):
        # Add the stock and price of two objects
        total_stock = self.stock + other.stock
        total_price = self.price + other.price
        return Stocks(total_stock, total_price)

print('--------------Vivo Stock----------------')
vivo = Stocks(20, 350000)
vivo.stockava('Vivo')

print('--------------Realme Stock----------------')
realme = Stocks(23, 475000)
realme.stockava('Realme')

print('--------------Samsung Stock---------------')
samsung = Stocks(15, 640000)
samsung.stockava('Samsung')

print("--------------Total Stock-----------------")
# First add vivo and realme, then add the result to samsung
total = vivo + realme + samsung

# Display the total stocks and prices
total.stockava('Total Mobiles and Their price ')
