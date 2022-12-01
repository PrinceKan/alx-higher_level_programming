#!/usr/bin/python3
a = ''
for i in range(122, 96, -1):
    if i % 2:
        a += chr(i - 32)
    else:
        a += chr(i * 1)
print('{}'.format(a), end='')
