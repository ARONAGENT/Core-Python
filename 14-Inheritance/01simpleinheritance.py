# simple inheritance -one derived class inherit one base class called as simple inheritance

#base class- Jo class inherit ho raha hai
class advancedDevloper:
    def advanceskills(self,sskill,hskill):
        print(f'advanced softskill :{sskill}')
        print(f'advanced hardskill :{hskill}')
#derived class -Jo class inherit kr raha hai
class coreDeveloper(advancedDevloper):
    def coreskill(self,name,sskill,hskill):
        print(f'Name           :{name}')
        print(f'core softskill :{sskill}')
        print(f'core hardskill :{hskill}')
print('-----------------------------------------devloper-1----------------------------------------')
ruchita=coreDeveloper()
ruchita.coreskill('ruchita','Do Exception handling and File handling','Oops')
ruchita.advanceskills('Do library handling and os modules','Djanjo anf mongodb')
print("------------------------------------------devloper-2--------------------------------------")
rohan=coreDeveloper()
rohan.coreskill('rohan','Do Exception handling and File handling','Oops')
rohan.advanceskills('html,css,javascript','spring,sprimg data jpa ,rest api')