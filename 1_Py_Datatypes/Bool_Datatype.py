# bool data type to represent logical values True and False
# valid values of bool in python are True and False
# true and false are not values in Python 

print(True) #output True
# print(true) #NameError: name 'true' is not defined. Did you mean: 'True'?

# True is defined as 1 internally  True == 1
print(True == 1) # output True
# False is defined as 0 internally

# if we do arithmatic operation with True and False 
# internally they will be treated as 1 and 0 
# arithmatic operation will happen based on that

print(True + True) # output 2
print(True - False) # output 1
print(False - True) # output -1

# Constructor: bool(x) converts x to a boolean following Python’s truthiness rules.
# bool() with no argument returns False.

b1 = True
b2 = False
b3 = bool(0)        # False
b4 = bool(1)        # True
b5 = bool("hello")  # True
b6 = bool("")       # False

# Truthiness rules (what counts as False)
# An object is considered False in a boolean context if it is one of:

# The boolean False itself.

# Numeric zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0,1).

# Empty sequences and collections: '', (), [], range(0), set(), frozenset(), dict(), bytearray(b''), bytes(b'').

# None.
# Everything else is considered True.

# learn about Truthiness.

#https://www.youtube.com/watch?v=fI51bSgB7rw&list=PLd3UqWTnYXOmzcSdWIh-EggqAtCXvJxzu&index=10