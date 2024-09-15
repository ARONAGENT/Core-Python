# in this example two exception occur to handle this we used two except 
try:
    x=int(input('Enter Numerator : '))
    y=int(input("Enter Denominator : "))
    print(f'Division is {x/y:.2f}')
# if the denominator in divison is 0 so cannot divide by zero so therfore it give ZeroDivisonError
#if the input is invalid so the value Error occur
except ZeroDivisionError: 
    print('cannot divide by zero')

except ValueError:
    print('invalid input plz enter a valid input')
      