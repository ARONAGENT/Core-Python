class desktops:
    def __init__(self,desnm,pronm):
        self.desttopname=desnm
        self.processorname=pronm
    
    def __str__(self):
        return f'Desktop name is {self.desttopname} and processor is {self.processorname}'
    
obj=desktops('Windows','I3')
print(obj)

# when  we used __str__ method  and something  return to that __str__ function 
# we can directly print the object using __str__ function 