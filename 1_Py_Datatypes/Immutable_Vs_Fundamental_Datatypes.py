# mutable  means changable
# immutable means non-changable

# everything in python is a object 

# in python if you change/modified existing value 
# python will allways create new object 
# in python all fundamental data types int,float,complex,bool,str 
# all are immutable
# why python fund data types are immutable?   
# becuase of object reusability concept of python.
# but this reusability is not supported by float and complex 
# in this 2 datatypes always new obj is created.

x = 10 # here x is reference variable here I assigned integer value 10
       #  to it so it will interger object x and it will point to value 10
x = 11 # here we are resuing a existing x integer object you might 
 # think new value 11 will replaced in the same object. No python doesn't
 # work like that it will create new integer object and point to it.
 # and the old object is gone for garbage collection.

y = 10
z = 10
k = 10 
print(id(y)) #140707430385048
print(id(z)) #140707430385048
print(id(k)) #140707430385048
print()
# note in python if we assign same content to a reference var 
# new object is not created instead other refernce var will start 
# pointing towards the same location. hence when I try to print address for 
# y and z variables it's same if we change any of them y or z new object will
# will be created for that 
# because of this reusability of objects increases hence memory efficient

# take a scenario you are building national id 
# for this state code is required
# started feeling data created var name city
# 1M people filled form from Pune
# and 1 person filled form for Mumbai 
# now without pythons feature of creating a new object for differnent 
# value what would have happen bcz of this single person 1M people 
# would have affected but in python we reuse only same content 
# so when this 1 person comes and fill form for Mumbai
# python will check in memory if Mumbai is present or not if not it will 
# create new object and it will point towards it.

person1city = "Pune"
person2city = "Pune"
person3city = "Pune"
person4city = "Mumbai"

print(id(person1city),id(person2city),id(person3city), sep="|")
print(id(person4city))

print(person1city is person2city) #True bcz both are pointing to same memory loc
print(person1city is person4city) #False

# special cases 
# 1) when reusing integers allowed in range of (o-256)
# so if we do 
num1 = 258
num2 = 258 
print(num1 is num2)   #True
#but If you create the integers at runtime 
#(so new objects are actually constructed), identity will 
# usually be False:

n1 = 1000.0
n2 = 1000.0
print(n1 is n2)
print(id(n1),id(n2), sep="|")

#Python creates and keeps a small set of integer objects 
# at interpreter startup. By default CPython preallocates 
# and reuses integers in the range -5 through 256 for the 
# lifetime of the process. Other integers are created on demand.
# same for bool two objects are created True and False


# Python reusablity at the
# int only in 0 to 256 ( may be optimize based on your configuraton) commonly used range
# bool allowed  
# str allowed 
# float not possible commonly used range cannot be defined 
# because between 0 and 1 there are infinite numbers so python
# can't decide fix range
# complex same as float 

# Why you sometimes see the same id() for floats/complex
# Short‑lived objects can reuse memory addresses. If you create a temporary float (e.g., id(1.1)) and it has no lasting reference, CPython may free that memory and the next temporary object can be allocated at the same address — making id(1.1) and id(2.2) appear equal in quick REPL checks. This is allocator reuse, not interning. 

# Compiler/bytecode optimizations can also fold literals in the same code block, which can make two identical literal occurrences share the same object in some contexts (this is separate from the small‑int cache). 