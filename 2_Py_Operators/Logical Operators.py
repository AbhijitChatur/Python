
# Logical Operators

# and  - if both args are True then only returns True
# or   -if at least one arg is True returns Ture
# not  - not True result in False opposite value

# they can be applied to boolean type and non boolean types 
# NOte if logical operators are applied to booleab types then result is always boolean


# for non-boolean types : 
# non-zero means True    we can call it truthy values
# empty string,obj ==> False      we can call them falsey values

# Case x and y 
# NOte if x evaluates to false then result is x otherwise returns yield

print(10 and 20) # 20 becuase here we are using logical and with non boolean
                 # and 10 is non zero so it means it is True and if it is True 20 will be retuned

print(0 and 20) # 0

print(1 and "Abhijit") # Abhijit 1 is non zero so y is return y is Abhijit

# case x or y
# if x is True then return x otherwise return y

print(100 or 0) # 100 here x is non zero so no need to evaluate y simply returns x
print(10 or 20) # 10 same here 
print(0 or 20) # 20 because x is false then will have to evaluate y and y is non zero so y is returned


def f1() :
    print("I am f1()", end="")
    
print(0 or f1())  # I am f1()None  f1() is evaluated because x is zero
print(1 or f1()) # 1 f1 is not evaluated bcz x is non zero so True

# case not x: always returns boolean value only
# not 10  # False bcz 10 is non zero internally this statement becomes
# not True so result is False
a = not 10
print(a) # False

# Shift Operators 
# << left shift operator 

# suppose you 10 << 2  convert 10  to binary 
# 8bit representation     00001010 now shift all bits to left by 2
#                         00101000 is the answer convert it to int 40

# same for right shift  just 

# 10>> 2  answer is 2 

# True << 2  anwer is 4  True is 1 internally shift bits by 2 
