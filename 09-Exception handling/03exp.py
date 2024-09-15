# here also occur two exception ValueError and IndexError but we can used common except block
lst=['mango','orange','apple','banana','grapes']
try:
    i=int(input('Enter a any index no of following list : '))
    print(f'Your item at {i} is {lst[i]}')
except:
    print('list out of bound plz enter a valid index')