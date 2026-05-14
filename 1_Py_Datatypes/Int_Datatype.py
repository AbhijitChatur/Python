# There are total 14 datatypes are available in Python

# Fundamental datatypes of python are 
# int float bool str complex

# python don't have char type char is defined as string in python so no seprate dataype of single characters.
# other datatypes of python are 
# list tuple dict set frozenset
# bytes bytearray range none 

# to know type of value use type() function
a = 10 
print(type(a))  # putput <class 'int'>
# to know address where a variable is stored in the memory use id function 
print(id(a)) # output 140708662330776
# to print you variable as a stdout use print()
print(a)  # output 10

#python 2 had a long data type but it became depricated in python 2 

# we can call int type as integral number as well
# there are total 4 ways to define integral number in python
# 1) is default - decimal number i.e base 10
# represented by (0-9)
# for example 13 , 32434, 32432423,
print("Default Decimal number")
b = 23232
print(b) # output 23232
#  2) binary number i.e base 2 represented by (0 and 1)
#   to initialise binary number to a variable will have use 
#   0B or 0b as prefix to our desired number i.e using only 0's and 1's
print("Binary")
c = 0B1100
print(c) #output 12
#print(type(c)) #int 
#  3) octal numbers i.e base 8 represented by (0 to 7)
#   to initialise octal number will have to use 
#   0O or 0o as prefix to our desired number i.e using only 0-7
print("octal number")
d = 0O3434
print(d) # output 1820
#   4) Hexadecimal number i.e base 16 represented by (0-9) & (A-F) or (a-f)
#   to initialise hexadecimal will have to use 
#   0X or 0x as prefix to our desired number i.e using only (0-9) & (A-F) or (a-f)
print("Hexadecimal number")
e = 0XAF
print(e) # output 175

################################
print('#'*60)
print("int base Conversion Functions in python")
print()
# why do we need base conversion function in python
# suppose you want to convert binary number to octal or
# hexadecimal or octal in hex or Binary for this 
# we need int base conversion functions
# 1) bin() to convert number in binary format
# 2) oct() to convert number in octal format
# 3) hex() to convert number in Hexadecimal format 
# Note:  we don't have any function to convert int in decimal format
# i.e bcz in python int are bydefault are in decimal format

f = 0b01
print(hex(f)) #output 0x1 
g = 0xA
print(bin(g)) # output 0b1010

# float data types : we can represent float values only in decimal 
# format i.e in base 10 and not in Binary or Ocatal or hexadecimal
# if we try to convert float values in Binary will get type error 
# h = 11.23 
# print(bin(h))TypeError: float obj cannot be interpreted as an integer

# Note we can declare float in Exponential format / Scientific format
i = 12.23e3 # we can use capital E as well like 23.2E2
print(i) # output 12230
# Note we can define float numbers in exponential format only. 

