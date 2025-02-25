import sys

n = len(sys.argv)
if (n != 2):
    print("You need to input only one number")
elif (sys.argv[1].isdecimal):
    if (int(sys.argv[1]) % 2 == 0):
        print("I'm Even")
    elif (int(sys.argv[1]) % 2 != 0):
        print("I'm Odd")
else:
    print("please provid a decimal input")