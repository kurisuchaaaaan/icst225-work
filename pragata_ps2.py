import sys

prog = sys.argv[0]
arg = sys.argv[1]
num = int(arg)

if num > 220:
    print("Super Typhoon")
elif num >= 188 and num <= 220:
    print("Typhoon")
elif num >= 89 and num <= 117:
    print("Severe Tropical Storm")
elif num >= 62 and num <= 88:
    print("Tropical Storm")
else:
    print("Tropical Depression")