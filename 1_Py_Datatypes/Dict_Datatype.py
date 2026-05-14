
# dict() 
# since Python 3.7 dict insertion order is preserved
# in the case of list,tuple,set,frozenset,range,bytes,bytearray 
# we store object in these datatypes as a group of individual 
# objects.

# in several above mentioned datatypes 
# like list,tuple,range,bytes and bytearray
# we use index to manipulate these objects 
# this index are allways start from 0 
# we cannot use any other indexing format

# when you want to use userdefined indexes
# we can use dictonary where we use user defined keys as indexes to 
# manipulate 

# In dictonary we use key - value pair 
# use dictonary when you want to allowed duplicates and order is preserved
# dict is mutable 

# representation of dict
d = {100:'Abhijit',200:'Shivani',300:'Ravi'}
# keys and values can be heterogenios
# keys cannot be duplicated
# values can be duplicates

# Note
d1 = {}
print(type(d1)) #<class 'dict'>
# if we represent {} empty parenthesis then 
# it is allways considered as dict by defalut
# if you want to create empty set then we can use
# s = set() we cannot s = {} it will be treated as dict

# since dict is mutable we can declare empty dict like d1 we decalred
# we can assign new keys value pair in dict
d1[1000] = 'Abhijit'
d1[1111] = 'Saurabh'
print(d1) #{1000: 'Abhijit', 1111: 'Saurabh'}

# in modern Python, dictionary order is preserved.
#  Starting with Python 3.6, insertion order was
#  maintained as an implementation detail, and 
# from Python 3.7 onward, it became part of the
#  official language specification. That means 
# when you iterate over a dict, keys will appear
#  in the order they were added.


s1 = {1,2,3}
s2 = {3,2,1}
s3 = {2,1,3}
print(s2 == s3) #True since order is not preserved


#https://www.youtube.com/watch?v=fI51bSgB7rw&list=PLd3UqWTnYXOmzcSdWIh-EggqAtCXvJxzu&index=10