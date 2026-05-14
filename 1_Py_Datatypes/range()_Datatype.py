
# range() datatype

# range data type represent a sequence of values 
# range is immutable

# there are multiple forms to represent  range()

# form 1 : range(10)
# ir represents values from 0 to 9

# range() is a function and datatype both we can say

r = range(10)
print(type(r)) # <class 'range'>

print(r) # range(0, 10)

# to print all numbers in this range(10)
# we can use for loop 
# if you want to print particular value we can use Index
print(r[5]) # 5
# slice is allowed
print(r[3:]) # range(3, 10)

# proof that range is immutable
r1 = range(10)
# r1[0] = 132 # error doesnot support assignment


# Form 2 to represent range()
# to start from and end at particular position
# range(10,30) this will represent 10 to 29 numbers

# Form 3: rage(10,50,5)
# range between 10 to 49 and step forward by 5
r2 = range(10,50,5)
for i in r2: print(i, end=" ") #10 15 20 25 30 35 40 45 

# Error : what if we use float values in range
# range(15.5,12.4)
# TypeError : float object cannot be interpreted as an integer
# becaue there are infinite numbers between two 

