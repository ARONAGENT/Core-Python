#this is the example of if inside if 
# this example look difficult to understand so we used elif code
age = 25
has_id = True

if age > 18:
    if has_id:
        print("You are allowed entry.")
    else:
        print("You need an ID.")
else:
    print("You are too young to enter.")