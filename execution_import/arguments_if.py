import sys

print(sys.argv)

if len(sys.argv) > 2:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print('result is', a+b)

