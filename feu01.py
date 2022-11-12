import sys

def build(h,w):
    top = "°" + "-"*(w-2) + "°"
    middle = "|"+ " "*(w-2) + "|"
    bot=top
    if h == 1:
        print(top)
    elif w==1:
        top="°"
        middle="|"
        bot="°"
        print(top)
        for i in range(h-2):
            print(middle)
        print(bot)
    else:
        print(top)
        for i in range(h-2):
            print(middle)
        print(bot)
    
try:
    w=int(sys.argv[1])
    h=int(sys.argv[2])
    if len(sys.argv) != 3 or w<=0 or h<=0:
        raise Exception
    if w ==1 and h==1:
        print("°")
    elif w==1 and h==2:
        print("°")
        print("°")
    else:
        build(h,w)

except Exception as e:
    print("erreur.",e)

