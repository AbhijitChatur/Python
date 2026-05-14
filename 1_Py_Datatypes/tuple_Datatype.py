
#tuple
l = [12,23,45,56] # list

# how to represent tuple in python
# by using () we can represent tuple

#t = () # empty tuple

# there is only 2 changes between list and tuple 
# there representation is differnt for list we use []
# for typle we use ()
# list is mutable(changable) tuple is immutable

t = (12,121,45,'Abhijit')
print(type(t), t) #<class 'tuple'> (12, 121, 45, 'Abhijit')

# slice operator
print(t[0:3]) # (12, 121, 45)

# modification is not allowed
# t[0] = 1232 # Typeerror tuple obj does not support item assignment

#  * operator
# yes allowed because here we are not changing the 
# content
print(t*2) # (12, 121, 45, 'Abhijit', 12, 121, 45, 'Abhijit')

# (10,20,[30,40])  here we have a 3 items in tuple not 4 
a = (10,20,[30,40]) 
print(a[2][1]) # 40
print(a[2][0]) # 30
print(a[2]) # [30, 40]


#https://www.youtube.com/watch?v=fI51bSgB7rw&list=PLd3UqWTnYXOmzcSdWIh-EggqAtCXvJxzu&index=10