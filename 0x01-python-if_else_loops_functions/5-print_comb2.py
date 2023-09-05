#!/usr/bin/python3
for i in range(0, 100):
    if i <= 9:
        i = '0' + str(i)
    if int(i) < 99:
        print(f'{i}', end=", ")
    else:
        print(f'{i}')
