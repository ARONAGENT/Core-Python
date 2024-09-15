# because of self keyword we can use global varibales in methods using self keyword otherwise it give error
class cricketPlayers:
    playnm='Virat kolhi'
    def showname(self):
        print('player name is',self.playnm)
    
obj=cricketPlayers()
obj.showname()