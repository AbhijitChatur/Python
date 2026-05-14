
# + -> Addition Operator
# - -> Subtraction Operator
# * -> Multiplication Operator
# / -> Divison Operator
# // Floor Division Operator
# % Modulo Operator   (Reminder)
# ** Exponent Operator or Power Operator

a = 10 
b = 2
print("a + b =",a+b)
print("a - b =",a-b)
print("a * b =",a*b)
print("a / b =",a/b)    # 5.0 Note (result of division operator is always float)
print("a % b =",a%b)  # 0
print("a // b =",a//b)  # 5 
print("a ** b =",a**b)  # 10^2 square  = 100



# if both numbers are int then result will be int 
# if any one of the number is float then result will be float
# in floor division result in rounded down to the rearest integer
print(11.9 // 2)  # 5.0 rounded down to nearest integer
print()
a1 = 10.0
b1 = 2
print("a1 / b1 =",a1/b1) #5.0
print("a1 // b1 =",a1//b1) #5.0

# diff / and //
# / always results in float 
# // if both num are int then ans is int 
#   if one of the num is float then ans is float 
#   // in floor divisor result is rounded down to nearest integer

# + can be used to concatenate str
s = "Abhijit"+"Chatur"
print(s) #AbhijitChatur
# rule both arguments must be str if "abhi" + 3 then results in error
# "abhi"+10 is error
# print("abhijit"+10) TypeError: can only concatenate str (not "int") to str

# * can be used with str 
# "abhi" * 3  result is abhi will be printed 3 times
# rule if you want to use * with str then 1 argument must be int
# cannot use * with 2 str
# float is not allowed 

# x/0 or x%0 or x//0 zerodivision error: division by zero

# 