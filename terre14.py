import sys

try:
    argv=sys.argv[1:]
    if len(argv) != 3 or argv[1]==argv[0] or argv[2]==argv[1] or argv[0]==argv[2]:
        raise Exception
    argv.sort()
    print(argv[1])
except Exception as e:
    print("erreur.",e)