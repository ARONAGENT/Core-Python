# Read data from CSV file
file=open('cars.csv','r')
data=file.read()
print(data)
file.close()
