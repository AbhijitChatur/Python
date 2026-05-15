
# There are so many different ways we can print out put 
# different combinations

# # print() prints empty line
print()

# print(str) pass string enclosed using quotes or str obj  
print("Hello") # Hello
s = "Hello"
print(s) # Hello
# we can do concatenation of two strings
print("Hello"+"World") # output is HelloWorld
print("Hello","World") # Hello World here there is a space between Hello World bcz
# python print() function has a sep=' ' argument and by default it takes space charater
# so all objects mentioned in print statements are seprated by space we can use any character or sequence of character to 
# seprate objects

# print with numbers and strings along with sep='' argument of print()
a1 = 123
print("Hello",a1,233)  #Hello 123 233
print("Hello",a1,233, sep='%%%%') # Hello%%%%123%%%%233

# print() function with end='' argument
# end='' print() end argument is used to tell the interpreter after printing this
# print statement what should happen
# so if we do print("Hello") here we didn't mention end arg still interpreter will
# add end arg with \n so this statements becomes print("Hello",end='\n')
# what does this mean after printing Hello controller must jump on next line
# so if we don't want to jump on new line we can pass empty string to end arg
print("Hello",end=' ')  # Hello World will print here and after that controller will jump on new line
print("World")          # bcz we didn't used end arg with this statement


#formatted string   
c=30   
print("a value is %i" %c)    #a value is 30
#print("a %i value is %i" %c)    #TypeError: not enough arguments for format string
print("a %i value is %i" %(c,c)) #a 30 value is 30
s = "Abhijit"
print("my name is %s"%s) #my name is Abhijit


# print() with replacement operator {} and .format

s1 = "Abhijit"
s2 = 234223
print("My name is {0} my mob number is {1}".format(s1,s2))
# My name is Abhijit my mob number is 234223
print("My name is {something} my mob number is {anything}".format(something=s1,anything=s2))
# My name is Abhijit my mob number is 234223
