import json
file=open('mobile.json','r')
data=json.load(file)
print(data)
file.close()