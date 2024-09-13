import json
mobile={
    'name':'Realme 5i',
    'ram':'4gb',
    'rom':'64gb',
    'processor':'Qualcom Snapdragon 665',
    'price':'11000'
}

file=open('mobile.json','a')
json.dump(mobile,file)
file.close()
print('JSON data inserted successfully')