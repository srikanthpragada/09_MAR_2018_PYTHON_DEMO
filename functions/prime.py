import sys
from math import sqrt

if len(sys.argv) == 1:
    print("Usage : python prime.py num ...")
    sys.exit(0)   #stop program

# print(type(sys.argv))
for i in range(1, len(sys.argv)):
    num = int(sys.argv[i])

    for n in range(2, int(sqrt(num) + 1)):
        if num % n == 0:
            print(num, "Not a prime number!")
            break
    else:
        print(num,"Prime number!")




