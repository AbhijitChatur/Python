
# Equality operator

# == , != 

# == always comapare the content of obj or variable
# to comapre address of obj or var use is operator

print(10 == 20) # False

print(10!=20) # True

print(10==True) # False

print(False==False) # True

print(10==10.0) # True  note as long as both datatypes are compatible to compare they will be evaluated based on content
print("abhi" == 'abhi')  # True

print(10 =="durga") # we never get error with equality 
#operator. we can pass any types of values if it is not compatible
# then will get False as a result

# chaining is allowed with equality op
# if atleat one comparison is false then answer is false
# if all are true then answer is True

# 'a' == 97 False  internally 'a' is not going to replace with Ascii value

# 1 == True  # True  internally True is 1