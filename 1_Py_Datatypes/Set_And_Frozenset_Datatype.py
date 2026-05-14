# suppose our requirement is duplicates are allowed and
# order is preserved then we can use list
# but if you don't want duplicates and you don't want
# order then use set()

# set() elements are represented using {object}

s = {10,20,30,10,20,30} # here no syntax error 
print(s) # {10, 20, 30} # 
#print(s[0])  # TypeError: 'set' object is not subscriptable
# we are getting error becuase in set order is not preserved so 
# we cannot gurrantee at which location our values are getting stored
# idexing is not supported by set datatype

# slicing is not allowed becuase indexing is not allowed
# order is not allowed 

# heterogenious objects are allowed
s1 = {12,"abhijit",12.2}
print(s1) # {12, 12.2, 'abhijit'}

# set is mutable so set is growable
s1.add('durga')
print(s1) #{'durga', 'abhijit', 12, 12.2}
s1.remove(12)
print(s1) # {'durga', 12.2, 'abhijit'}
# here you can see order is not preserved

# Frozenset()

# Only diff between set adn frozenset is frozenset are
# immutable.
# How to represent frozenset
s = {10,20,30,40}
fs = frozenset(s)
print(type(fs)) # <class 'frozenset'>
# fs.add(34) # attributeerror : frozenset object has no attribute add

# when to use frozenset 
# when you don't want to preserved order and want object to be 
# immutable then use frozenset
# except above 2 propeties everything between set and frozenset is same

