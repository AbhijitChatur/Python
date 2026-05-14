
# Bitwise Operator:

# &   
# |
# ^
# ~
# <<
# >>

# This operators are applicable with only int and boolean

# 4&5  -> valid
# True & False -> valid
# 10.5 & 23.3  -> not valid  type error unsupported perand for (&) float & float

# & --> if both bits are 1 then only 1 otherwise 0
# | --> if atleast one bit is 1 then 1 otherwise 0
# ^ --> xor if both bits are different then 1 otherwise 0
# ~ --> bitwise complement operator
#     1 == > 0 and 0 ==> 1

# << --> bitwise left shift
# >> --> bitwise right shift

# & bitwise and
b = 4 & 5 # here internally 4 and 5 converted into binary 
# 4 = 100
# 5 = 101
# &   100        here perform and operation between 4 and 5 will get 4 
print(b) #4

# | bitwise or
b1 = 4 | 5      #here perform and operation between 4 and 5 will get 101 i.e 5
print(b1) #5

# ^ bitwise x-or
b2 = 4 ^ 5
# 4 = 100
# 5 = 101
# ^   001                  # if both bits are different then 1 otherwise 0
print(b2)  # 1 if both 

# bitwise complement operator (~)
b3 = ~4
# internarlly 32 bit or 64 bit 
print(b3) # -5