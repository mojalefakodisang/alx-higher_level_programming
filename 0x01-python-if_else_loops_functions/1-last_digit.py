#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_number = str(number)
str1 = "Last digit of " + str_number + " is "
str2 = str_number[-1]

if int(str_number[-1]) > 5:
    print(str1 + str2 + " and is greater than 5")
elif int(str_number[-1]) == 0:
    print(str1 + str2 + " and is 0")
elif int(str_number[-1]) < 6 and not int(str_number[-1]) == 0:
    print(str1 + str2 + " and is less than 6 and not 0")
