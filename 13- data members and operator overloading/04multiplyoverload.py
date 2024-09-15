class workingdaysAndmonth:
    def __init__(self,days,month):
        self.days=days
        self.month=month
    
    def calcsalary(self,name):
        print(f'user name     :{name}')
        print(f'days          :{self.days}')
        print(f'month         :{self.month}')
    
    def __mul__(self,s):
        dayss=self.days*s.days
        monthss=self.month*s.month
        print(f'total multiplication days  :{dayss}')
        print(f'total multiplication month :{monthss}')
    
print('--------------User 1----------------')
rohan=workingdaysAndmonth(60,2)
rohan.calcsalary('Rohan Uke')
print('--------------User 2----------------')
rahul=workingdaysAndmonth(90,3)
rahul.calcsalary('Rahul thakare')
print("--------------Total multiplcation of Users-----------------")
total=rohan * rahul