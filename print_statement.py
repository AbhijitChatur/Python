# Basic
print("Hello, World!")            # prints with newline

# Multiple objects and custom separator
print("A", "B", 123, sep=" | ")   # A | B | 123

# Avoid newline
print("Progress:", end=" ")
print("50%")

# Redirect to file
with open("out.txt", "w") as f:
    print("Saved line", file=f)

# Print to stderr
import sys
print("Error occurred", file=sys.stderr)

# Force immediate flush (useful in logs/CI)
print("Flushed now", flush=True)

# f-strings for formatted output (Python 3.6+)
name = "Abhijit"
print(f"Hello, {name} — {2026}")

lst = [1, 2, 3]
t = ("A", "B")
s = "Python"
print(lst, t, s) #The function prints all objects in one line separated by the default space because sep=" ".

# print(sep=" | " , 12, 12) No — this call is invalid. 
# In Python you must place positional arguments (the objects to print) 
# before any keyword arguments. Putting a keyword argument like sep= before positional 
# values raises a SyntaxError (positional argument follows keyword argument).


# When to use which parameter
# sep — change how multiple objects are joined (default space). 
# end — change trailing character (default \\n). Use end='' to stay on same line. 
# file — pass any object with a .write() method (files, io.StringIO, sys.stderr). 
# flush — set True to bypass buffering and write immediately (important for real‑time logs). 
                       
import keyword
print(keyword.kwlist)

a  = "durga" * 0x122
print(a)
