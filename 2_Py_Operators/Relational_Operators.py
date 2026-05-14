
# Relational Operators

# >,<,>=,<=


# note when comapring two str result will be based on 
# the alphabetical order below abhijit and chatur   a ascii value is lower than c
# hence 
s1 = "abhijit"
s2 = "chatur"
print(s1>s2) #False
print(s1>=s2) #False
print(s1<s2) # True
print(s1<=s2) # True

# if you compare A > a then A ascii value is 65 and a ascii value is 97
s3 = 'A'
s4 = 'a'
print(s3>s4) #False

# chaining of relational operator is allowed
# 10<20<30<40 is True
# if one expression is false then false is the anser no matter what
# 10<20<30>50   is False
# 10<20<35>30   is True


# we can use relational op with str
# result will be based on ascii
s5 = 'A'
s6 = 'a'
print()
print(s5>s6)  #False
print(s5<s6)  #True

# we can do 10 > True as long as one value is True or False we will get result

# we can't do 10 > "abhijit"

