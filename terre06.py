import sys

try:
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    print("resultat: ",a//b)
    print("reste: ",a%b)
except Exception as e:
    print("erreur.")

    