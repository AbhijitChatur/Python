# int()
# float()
# complex()
# bool()
# str()

# int(): 
# 1) convert float to int (possible)
print(int(123.456)) #123

# 2)convert complex to int (not possible)-> complex is not compatible with int
# if we try to convert complex type to int type 
# will get typeerror can't convert complex to int

# 3)bool to int (possible)
print(int(True)) # 1

# 4) str to int (possible)
print(int("10")) # 10 whole numbers only 
#print(int("10.5")) # valueerror : invalid literal for int()
                   # int() with base 10: '10.5'
# when converting str to int the string should be integer and 
# with base 10 value only No Binary,Octal,hex allowed, float
#print(int("hello")) error
print()

#=============================================================

# float()
print("float()")
# 1) int to float (possible)
print(float(10))   # 10.0
# 2) complex to float (not possible)
# 3) bool to float (possible)
print(float(False)) # 0 
# 4) str to float (possible) 1 pitfall
# while converting str to float value must be integral or floating type inside quotes
# float(binary octal hex are not allowed)
print(float("10.0"))  # 10.0   
# print(float(ten))    error
# print(float("0b11101")) error


#=============================================================

#Complex() - converting other datatypes into complex
# 2 complex() functions are available in python
print()
print("Complex")

# 2 cases complex(x) and complex(x,y)
# when we pass single argument to complex(x)
# x becase real part of complex datatype i.e x+0j
s = 10
print(complex(s))  # (10+0j)

# if we pass 2 arguments then complex(x,y)
t = 10
u = 20 
print(complex(t,u)) #print(complex(t,u))

# complex(bool value)
# complex(True)  output is 1+0j
# complex(False) output is 0j
print(complex(True,False)) # (1+0j)
# and as we know real part and img part of complex data type 
# can be integer(binary,octal,decimal), float

v = 0x1A
w = 0b11
print(complex(v,w)) # (26+3j)


# there is trick instead of defining complex data types 
# with binary and octal and hex  like this
# a= 10 + 0b11*j we will get error j is not defined
# in this case we can use complex(x,y)
# will definned real part and imag part then pass it to complex()
realpart = 0X12A
imagpart = 0B11
print(complex(realpart,imagpart)) # (298+3j)


# complex("10") 
print(complex("10")) # (10+0j)
print(complex("10.5")) #  (10.5+0j)
# realpart1 = "10"
# imagpart1 = "10.5"
## Impoatant only keep this in mind : 
# second argument to complex(real,imag) must be numeric value.
# print(complex(realpart1,imagpart1)) Typeerror : 
# Complex() can't take second arg if first is a string
# so passing 2 str into complex(x,y) is not allowed if first argument is str then shouldn't send second argument
# If you call complex(realpart1, imagpart1) with 
# both arguments as strings, Python raises a 
# TypeError because the second argument cannot be a string.
# Correct ways to do it
complex('3+4j') # is allowed
#complex() accepts one string that is a valid
#  complex literal (decimal notation with j), 
# parses it, and returns the complex number (3+4j).


# 1. Convert the strings to numbers first

# python
realpart1 = "10"
imagpart1 = "10.5"

z = complex(int(realpart1), float(imagpart1))
print(z)        # (10+10.5j)

# complex("Hello") # valueError
# complex("0B111") # valueError


########################################################
print()
print("bool() conversion")

bool(0) # False
bool(1) # True
bool(-10) # True
bool(10.2)  # True
bool(0.001) # True
bool(0.0) # False
bool(complex)
bool("False") # True got You?
bool(10+20j) # if both real and img part are  zero
# then False otherwise True even single part is non zero
bool(str) # if we pass empty string then false in any other cases it is True


##################################################################

print()
print("str()")

str(10) # '10'
str(10+20j) #'10+20j"
str(True) # 'True'
str(3+4j) #  #"(3+4j)" got you?
#we can pass any data type to str() is possible
