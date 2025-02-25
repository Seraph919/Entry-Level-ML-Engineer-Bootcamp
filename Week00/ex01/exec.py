import sys

n = len(sys.argv)
if (n != 1):
    string = sys.argv[1]
    for x in range(2, n):
        string+=" "
        string+=sys.argv[x]
    string = string.swapcase()
    rsring = string[::-1]

    print(rsring)