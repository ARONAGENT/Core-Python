# multiple inheritance -one derived class inherit more base class called as multiple inheritance

#base class- Jo class inherit ho raha hai
class advancedDevloper:
    def advanceskills(self,sskill,hskill):
        print(f'Advanced softskill :{sskill}')
        print(f'Advanced hardskill :{hskill}')
#base class -jo class inherit ho raha hai
class systemdeveloper:
    def systemdeveloperskills(self,skills,systype):
        print(f'System developer skill  :{skills}')
        print(f'Which System mainly used :{systype}')

#derived class -Jo class inherit kr raha hai
class coreDeveloper(advancedDevloper,systemdeveloper):
    def coreskill(self,name,sskill,hskill):
        print(f'Name           :{name}')
        print(f'Core softskill :{sskill}')
        print(f'Core hardskill :{hskill}')


print('-----------------------------------------devloper-1----------------------------------------')
ruchita=coreDeveloper()
ruchita.coreskill('ruchita','Do Exception handling and File handling','Oops')
ruchita.advanceskills('Do library handling and os modules','Djanjo anf mongodb')
ruchita.systemdeveloperskills('Architecture design,database design','linux')

print("------------------------------------------devloper-2--------------------------------------")
rohan=coreDeveloper()
rohan.coreskill('rohan','Do Exception handling and File handling','Oops')
rohan.advanceskills('html,css,javascript','spring,sprimg data jpa ,rest api')
rohan.systemdeveloperskills('API design , microservices architecture','windows')