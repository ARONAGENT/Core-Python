# static method are belongs to class not and object 
# also we dont take self in argument because we dont need call reference of object 
# because static method are independent of object 
# we can call static method without creating objects of that class .
# we call with classname.method()  
class names:
    
    @staticmethod
    def personnmage(nm,age):
        print(f'your name is {nm} and age is {age}')
    
    @staticmethod
    def calcube(no):
        cube=no*no*no
        print(f'Cube of {no} is {cube}')


names.personnmage('Rohan',19)
names.calcube(9)