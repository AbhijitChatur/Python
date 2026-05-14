
# special operators in Python 
# Identity (is and is not)
# membership (in and not in)

# When to use identity
# use Identity operator when you want to check if 
# two object are pointing to same memory location
# Identitiy operator doesn't compare content 
a = 10 
b = 10.0
print(a is b) # False

# because a and b are pointing towards different memory lcoation
 
# if you want to compare content of two objects
# then use == operator

print(a==b) # True
print(10 == '10') # in some cases datatype matters

# there is also is not operator
# is not returns True if both objects are poiting 
# towards different location in the memory

s1 = 232
s2 = 232.0
print("is not demo ",s1 is not s2) # True


# membership operator (in) and (not in)
# when to use? when you want to check if certain Value 
# is available in some object or not then use membership 
# operator 

l = [23,34,5343,534,3]
print(5343 in l) # True 


s = "Hello, How are you doing?"
print('Hello' in s) # True
print('?' in s) # True character level if pass any other char remember python is case sensitive 

