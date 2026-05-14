
# accpet 4 cmd argument add them and display the sum

from sys import argv

args = argv[1:]
sum = 0

for x in args:
    sum  = sum + int(x)

print("the sum of numbers is: ",sum)