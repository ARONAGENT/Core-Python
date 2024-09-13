file=open('cars.csv','a')
nm=input('Enter carnm :')
price=input('enter  car price :')
comnm=input('Enter company name :')
typ=input('Enter type of car :')
data=f'{nm},{price},{comnm},{typ}'
file.write(data+'\n')
file.close()
print('CSV data inserted successfully')
