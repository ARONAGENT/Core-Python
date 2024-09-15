# Red the data from JSON file
import json # we have to import module for json to handle json files
file=open('mobile.json','r')
data=json.load(file) #load() method is used to read the data from JSOn file
print(data)
file.close()