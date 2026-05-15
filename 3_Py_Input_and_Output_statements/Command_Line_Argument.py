# This argparse module topic is very helpful when writing scripts that we will execute in Linux without GUI.

# The argparse module in Python is the standard way to handle command-line
# arguments—it lets you define inputs, options, and flags for your script, 
# automatically generates --help text, and handles errors gracefully. 
# Think of it as a way to make your Python programs behave like Linux 
# commands such as ls or cp

# how to use it 

# import argparse

# #Create a parser object:
# parser = argparse.ArgumentParser(description="Demo of argparse")
# parser.add_argument('-n','--number1', required=True, help="Enter no 1")
# parser.add_argument('-N','--number2', required=True, help="Enter no 2")
# args = parser.parse_args()

# print(args)

####################################################################################################################

# positional arguments
# if arg not passed will get error 
# usage: [-h] number1 number2 Operation
# : error: the following arguments are required: Operation
# to make argument optional so will not error even if we don't send it 
# just add "--number1"  just two -- to name of argument


# import argparse

# parser = argparse.ArgumentParser("")
# parser.add_argument("number1", help="Enter first number")
# parser.add_argument("number2", help="Enter 2nd Number")
# parser.add_argument("--Operation", help="Enter arithmatic operation you want to perform")
# args = parser.parse_args()
# x = int(args.number1)
# y = int(args.number2)
# o = args.Operation

# if(o == '+'):
#     print(f"sum of {x} and {y} is ",x+y)
# elif(o == '-'):
#     print(f"sub of {x} and {y} is ",x-y)
# elif(o == '*'):
#     print(f"Mul of {x} and {y} is ",x*y)
# elif(o == '/'):
#     print(f"Div of {x} and {y} is ",x/y)
# else:
#     print("User didn't mention Opeartion to be perfomr.")  # C:\OneDrive\Desktop\2026\Python\Python\3_Py_Input_and_Output_statemetns>python Command_Line_Argument.py 3 4
                                                           # User didn't mention Opeartion to be perfomr. bcz we made operation as optional using by adding -- to the prefix of argument name
    
# C:\OneDrive\Desktop\2026\Python\Python\3_Py_Input_and_Output_statemetns>python Command_Line_Argument.py -h
# usage: [-h] number1 number2 Operation

# positional arguments:
#   number1     Enter first number
#   number2     Enter 2nd Number
#   Operation   Enter arithmatic operation you want to perform

# options:
#   -h, --help  show this help message and exit

# C:\OneDrive\Desktop\2026\Python\Python\3_Py_Input_and_Output_statemetns>python Command_Line_Argument.py 3 4 *
# Mul of 3 and 4 is  12

# C:\OneDrive\Desktop\2026\Python\Python\3_Py_Input_and_Output_statemetns>python Command_Line_Argument.py 3 4 -
# sub of 3 and 4 is  -1

# C:\OneDrive\Desktop\2026\Python\Python\3_Py_Input_and_Output_statemetns>python Command_Line_Argument.py 3 4 +
# sum of 3 and 4 is  7

###########################################################################################################################


#lets say you clearly want to say please enter input from 
# the collection of choices only don't enter anything else 

import argparse

parser = argparse.ArgumentParser("")
parser.add_argument('-n',"--number1", help="Enter first number")
parser.add_argument('-N',"--number2", help="Enter 2nd Number")
parser.add_argument('-o',"--Operation", help="Enter arithmatic operation you want to perform" , choices=['+','-','*','/'])
args = parser.parse_args()
x = int(args.number1)
y = int(args.number2)
o = args.Operation

if(o == '+'):
    print(f"sum of {x} and {y} is ",x+y)
elif(o == '-'):
    print(f"sub of {x} and {y} is ",x-y)
elif(o == '*'):
    print(f"Mul of {x} and {y} is ",x*y)
elif(o == '/'):
    print(f"Div of {x} and {y} is ",x/y)
else:
    print("User didn't mention Opeartion to be perfomr.") 

# C:\OneDrive\Desktop\2026\Python\Python\3_Py_Input_and_Output_statemetns>python Command_Line_Argument.py 3 4
# usage: [-h] [-n NUMBER1] [-N NUMBER2] [-o {+,-,*,/}]
# : error: unrecognized arguments: 3 4

# C:\OneDrive\Desktop\2026\Python\Python\3_Py_Input_and_Output_statemetns>python Command_Line_Argument.py -N 11 -n 2 -o *
# Mul of 2 and 11 is  22

# what does help show for above program 
# C:\OneDrive\Desktop\2026\Python\Python\3_Py_Input_and_Output_statemetns>python Command_Line_Argument.py -h
# usage: [-h] [-n NUMBER1] [-N NUMBER2] [-o {+,-,*,/}]

# options:
#   -h, --help            show this help message and exit
#   -n, --number1 NUMBER1
#                         Enter first number
#   -N, --number2 NUMBER2
#                         Enter 2nd Number
#   -o, --Operation {+,-,*,/}
#                         Enter arithmatic operation you want to perform
