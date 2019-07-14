import random

def ran(low,high):
    number=int(input("enter the total numbers to be generated"))
    for i in range(number):
        yield random.randint(low,high)

for i in ran(1,20):
    print(i)