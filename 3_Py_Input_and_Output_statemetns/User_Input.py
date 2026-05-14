
# in python when accpeting input from user is always of str 
# type so always wrap input() inside preferred datatype function

print(type(input("Enter number and will check it's data type : ")))

x = int(input("enter any number: "))
y = int(input("enter any number: "))

min = x if x<y else y
print(x)