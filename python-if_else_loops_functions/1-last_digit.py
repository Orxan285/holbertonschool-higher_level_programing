#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numberLast = number % 10

if number < 0:
    numberLast = -(abs(number)%10)
if numberLast > 5:
    text = "and is greater than 5"
elif numberLast == 0:
    text = "and is 0"
else:
    text = "and is less than 6 and not 0"
print(f"last digit of {number} is {numberLast} {text}")
