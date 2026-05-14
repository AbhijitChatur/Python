# bytes data type:
# we can use it when handling video and audio like binary data
# it represents a group of byte values just like an array
# constraint - only in the range of 0 to 256 is allowed


a = [10,34,55,89]   
b = bytes(a)       # [10,34,55,89] all below to 256 valid
print(b[0],type(b)) #10 <class 'bytes'>

c = [11, 23,300]
#d = bytes(c) # ValueError: bytes must be in range(0, 256)

# bytes are immutable 
e = [10,20,30,40]
f = bytes(e)
print(f[0]) # 10

#f[0] = 122 # TypeError: 'bytes' object does not support item assignment
# hence bytes are immutable 

# bytes and bytearray
# there is a small diff between these datatypes
# bytes are immutable and valid in the range of 0 to 256
# but bytearray comes with advanced feature 
# bytearray are mutable and same range of bytes (o to 256) allowed
# to convert datatype into bytearray use bytearray()

g = [66,33,12,44] #  allowed range for bytearray 0 to 256
h = bytearray(g)
print(type(h),h[0])
h[0] = 122     # mutable modifying 
print(h[0])


#https://www.youtube.com/watch?v=fI51bSgB7rw&list=PLd3UqWTnYXOmzcSdWIh-EggqAtCXvJxzu&index=10