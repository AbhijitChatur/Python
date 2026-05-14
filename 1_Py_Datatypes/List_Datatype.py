# list of datatype
# insertion order is preserved
# duplicates are allowed
# heterogenious objects are allowed
# growable
# hence mutable
# represented using [] 


# When you want to represent a group of values 
# as a single entity where insertion order is preserved
# and duplicates are allowed use list data type.
# values must be defined inside []
# access values using index from left to right use 0 to .. and for right to left
# use negative index start from -1 to ...

# syntax l = [] empty list
l = []
type(l)   # <class 'list'>

# to add an object to existing list use .append(obj)
l.append(10)
l.append(20)
l.append(30)
l.append(10)

print(l) #[10, 20, 30, 10]
# here insertion order is preserved you can see and 
# duplicates are allowed.

# heterogenious objects are allowed 
# different types of datatypes are allowed
l.append("Abhijit")
print(l) # [10, 20, 30, 10, 'Abhijit']

# null is not allowed equivalent None is allowed
l.append(None)
print(l) #[10, 20, 30, 10, 'Abhijit', None]

# list object is growable we can increase or decrease the size of list
print(l[-1]) #None

# slice operator is allowed in list
print(l[1:5])

# * operator with list
s = [12,'Abhijit','Python']
s1 = s * 2
print(s1) #[12, 'Abhijit', 'Python', 12, 'Abhijit', 'Python']
