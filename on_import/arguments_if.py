import sys

print(sys.argv)

if len(sys.argv) == 1:
    print('необходимо два числа') 
    exit()

if len(sys.argv) == 2:
    print('не хватает второго числа')
    exit()

a = int(sys.argv[1])
b = int(sys.argv[2])
print('result is', a+b)
exit()



