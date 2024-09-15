dic={
    'name':'rohan',
    'age':19,
    'hobby':['playing cricket','watching web series','coding']
}
keys=input('enter a key : ')
try:
    print(dic[keys])
#if the key is not present in dictionary it give KeyError
except KeyError:
    print('Invalid key plz enter a valid key')
     
    