# write JSON type data in JSON file
import json # we have to import module for json to handle json files
mobile={
    'name':'Realme 5i',
    'ram':'4gb',
    'rom':'64gb',
    'processor':'Qualcom Snapdragon 665',
    'price':'11000'
}

file=open('mobile.json','a')
json.dump(mobile,file) # dump() method is used to write the data in JSON format in JSON File.
file.close()
print('JSON data inserted successfully')