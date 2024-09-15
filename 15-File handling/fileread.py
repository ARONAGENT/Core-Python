# read data in first.txt file 
file=open('first.txt','r')# r stands for read mode
info=file.read()
print(info)
file.close()
print("data read successfully")