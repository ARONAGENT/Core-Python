# Using elif: Instead of multiple if conditions, use elif where appropriate.
marks=int(input("enter marks"))
if(marks>90):
    print("grade A+")
elif(marks>80):
    print("grade A")
elif(marks>70):
    print("grade B")
elif(marks>60):
    print("grade C+")
else:
    print("grade D")    