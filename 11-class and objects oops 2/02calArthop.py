# self keyword->The self keyword in Python refers to the current instance of a class,
# allowing access to its attributes and methods.
# It ensures that each object of the class can maintain its own data and behavior independently.
# --------------------------------------------------------------------------------------------
# An instance of a class is an individual object created from a class blueprint. When a class is defined,
# it serves as a template,
# and creating an instance means creating an object that has its own unique data and can use the class’s methods.
class Calculator:
    def set_values(self):
        self.a = int(input('Enter first number: '))
        self.b = int(input('Enter second number: '))
    
    def add(self):
        result = self.a + self.b
        print(f'Addition of {self.a} + {self.b} is {result}')
    
    def sub(self):
        result = self.a - self.b
        print(f'Subtraction of {self.a} - {self.b} is {result}')
    
    def mul(self):
        result = self.a * self.b
        print(f'Multiplication of {self.a} * {self.b} is {result}')
    
    def div(self):
        if self.b != 0:
            result = self.a / self.b
            print(f'Division of {self.a} / {self.b} is {result:.2f}')
        else:
            print('Division by zero is not allowed')

obj = Calculator()
obj.set_values()
obj.add()
obj.sub()
obj.mul()
obj.div()
