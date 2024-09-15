try:
    file=open('bsb.txt','r')# r stands for read mode
    info=file.read()
    print(info)
    file.close()
    print("data read successfully...")
except FileNotFoundError: #if file not found this exception occur
    print('no such file or directory plz enter a valid filename ')
