import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"
letter=sys.argv[1]

for i in alphabet:
    if(letter <= i):
        print(i,end="")
    