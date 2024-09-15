try:
    nm=int(input('Enter a no :'))
    sq=nm*nm
    print(f'Square of {nm} is {sq}')
    
except ValueError: #if the input is invalid so the value Error occur
    print('input mismatch exception plz enter a valid input')

finally: #finally block always executable if the error occur of if the error not occur
    print('thank !')