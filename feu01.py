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
    width=int(sys.argv[1])
    height=int(sys.argv[2])
    if len(sys.argv) != 3 or width<=0 or height<=0:
        raise Exception
    if width ==1 and height==1:
        print("°")
    elif width==1 and height==2:
        print("°")
        print("°")
    else:
        build(height,width)

except Exception as e:
    print("erreur.",e)

