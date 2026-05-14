# str data type slice operator 
# this is a very useful operator to do many different tricks 
# with python str
    
# slice operator takes total 3 operators 
# for now will look in to 2 of them 
# those are begin and end 

# as name suggest slice operator is used to extract 
# substring/part of string 
# since to work with str we need str and index start from 
# 0 suppose you want to print last characters we can use 
# either negative index or we can use len(var name)-1 function 

a = "Abhijit"
# extract Abhi from above str a hint a[begin:end-1]
print(a[0:4]) # output Abhi  end-1  i.e 3
print(a[0:7]) # Abhijit

# here we don't have define begin or end if you want to use their
# default values.
# if you leave begin empty then it will be treat as 0 as default
# if you leave end as empty then it will be treated as end of str

# extract jit from a 
print(a[4:]) # jit

# if we do a[:] it means 0  to end and it will print exact str as it is

# if we use a[0:1000]
# you might think will get index out of range or some similar type of error 
# but we will not get such type of error 
# python simply print str from 0 position to till whatever number of sequence characters are there
#
# you might think if we do a[5 : 1]
# in this case as well will not any error 
# python will simply output empty str sinice 1 index doesn't appear after 5 
b = "Abhijit"
print(b[5:1]) # output empty line


# Slice operator application 
# 1) you have a name = abhijit
# you want to make first letter and the rest as it is
c = "abhijit"
print(c[0].upper() + c[1 : 8]) # Abhijit

# 2) you want to make last letter as Cap 
print(c[0:6] + c[-1].upper()) # abhijiT

# 3) now want to make first and last letter as cap and middle part as it is
print(c[0].upper() + c[1:6] +c[-1].upper()) # AbhijiT


# Important 3rd argument of slice method is step
# s[begin : end : step]
# 

s = "HElloletslearnPython"
print(s[0:12:2]) 
# Hloese here new str start from 
#0 and jumps by it will count from next 
#char 2 times and on the char where 2 lands 
# it will print that char 
print(s[0:12:3]) # Hlel

