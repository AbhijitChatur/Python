# Complex data  type declared as c = a + bj
# here we can use either j or J no other letter is allowed

# in above c complex variable 
# a is a real part 
# b is a imaginary PendingDeprecationWarning

# a can be int(decimal,Binary,Octal OR hexadecimal), float
# b can be int like a and float as well

# we can use .real to return real part
# and .imag to return imaginary part

#Type of parts: real and imag are floats even if created from integers.
a = complex(2,3)
print(a.real)

b = 12 + 30j
print(b.imag)

#z = True + False * j   # becomes (1+0j)
z = 2.5 + 1.7j
print(z)

# Using integer literals directly
# z1 = 0b101 + 0b10j      # binary: 5 + 2j
# z2 = 0o12 + 0xA*j      # octal 10 + hex 10j -> (10+10j)
# z3 = complex(0xFF, 0b1) # (255+1j)

# print(z1)  # (5+2j)
# print(z2)  # (10+10j)
# print(z3)  # (255+1j)
# print(type(z1.real))  # <class 'float'>

realpart  = 20 
imgpart   = 0b111
print(complex(realpart,imgpart))


#https://www.youtube.com/watch?v=fI51bSgB7rw&list=PLd3UqWTnYXOmzcSdWIh-EggqAtCXvJxzu&index=10