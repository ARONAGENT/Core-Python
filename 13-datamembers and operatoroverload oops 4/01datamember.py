#In Python, data members (also known as attributes) are variables that belong to an object or class.
# They store data that is associated with a particular instance of a class (instance variables)
# or the class itself (class variables).
class pens:
   #class varibale - global variable
    pen1='pentonic'
    pen2='butterflow'
    pen3='trimax'

    def func1(self,pen1,pen2,pen3):
        lst=[]
        # here pen1 ,pen2 pen3 are local variable -instance varibale
        lst.append(pen1)
        lst.append(pen2)
        lst.append(pen3)
        print(lst)

obj=pens()
obj.func1('flair','octane','cello')

# Or

class pen:
    def __init__(self,pen1,pen2):
        self.pen1=pen1
        self.pen2=pen2
    def func2(self):
       print(self.pen1)
       print(self.pen2)
    
obj2=pen('finegrip','cellogrip')
obj2.func2()