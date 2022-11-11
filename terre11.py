import sys

try:
    a=int(sys.argv[1])
    premier = True
    if len(sys.argv) != 2 or a<0:
        raise Exception
    if a ==1 or a==0:
        print(f"Non, {a} n’est pas un nombre premier.")
    else:
        for divisor in range(2,a):
            if a%divisor == 0:
                premier = False
                print(f"Non, {a} n’est pas un nombre premier.")
                break
        if premier : print(f"Oui, {a} est un nombre premier.") 
            
except Exception as e:
    print("erreur.")