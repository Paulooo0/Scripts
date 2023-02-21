import sys

if len(sys.argv) < 2:
    sys.exit('too few arguments')

print('hello, my name is ',end='')
for arg in sys.argv[1]:
    print(arg)
print('hello, your name is ',end='')
for arg in sys.argv[2]:
    print(arg)
print('hello, our name is ',end='')
for arg in sys.argv[1:]:
    print(arg,end=' ')