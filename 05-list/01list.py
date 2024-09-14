#List
#1.Ordered and mutable collection of elements.
#2.Can contain elements of different data types.
#3.Elements can be accessed, modified, added, or removed by index.
#4.Created using square brackets [].
#5.Versatile and commonly used for storing sequences.
lst=[]
print(type(lst))

lst.append("Bmw")
lst.append("Audi")
lst.append("Rolls Royal")
print(lst)

lst.remove("Bmw")
print(lst)

lst.insert(0,"forturner")
print(lst)

