import sys

try:
    nomber=int(sys.argv[1])
    if nomber%2 == 0:
        print("pair")
    else:
        print("impair")
except Exception as e:
    print("Tu ne me la mettras pas à l’envers.")

    