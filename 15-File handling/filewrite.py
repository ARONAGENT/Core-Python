#write txt into first.txt file 
file=open('first.txt','a') # a stands for append mode
data=input('Enter string :')
file.write(data+'\n')
file.close()
print('data inserted successfuly')