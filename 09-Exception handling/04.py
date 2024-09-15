 # here a is not initilaized hence the name error occur
try:
    a
    print(a)
except NameError:
    print('a is not defined plz initialized ...')