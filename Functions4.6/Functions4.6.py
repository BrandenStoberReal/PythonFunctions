import os
import math
import random

Names = [];
#Functions for 4.6
def compare(Number1, Number2):
    if (Number1 < Number2):
        print(str(Number2) + " is bigger then " + str(Number1))
    elif (Number1 > Number2):
        print(str(Number1) + " is bigger then " + str(Number2))
    else:
        print(str(Number1) + " and number " + str(Number2) + " are equal!")

def eliminate(num):
    for _ in range(random.randint(1, 100)):
        random.shuffle(Names)
    for _ in range(int(num)):
        Names.pop(random.randint(0, len(Names) - 1))
    return Names

for _ in range (3):
    Int1 = input("Please put in a number: ")
    Int2 = input("Please put in a second number: ")
    compare(int(Int1), int(Int2))


#Part 2

for _ in range(6):
    Name = input("Please give me a name: ")
    Names.append(Name)

NumOfPeople = input("How many people would you like to vote off the island?: ")
Remaining = eliminate(NumOfPeople)
CompiledString = "";

for i in range (len(Names)):
    if (len(Names) - 1 == i):
        CompiledString = CompiledString + "and " + Names[i]
    else:
        CompiledString = CompiledString + Names[i] + ", "

print("The remaining people are: " + CompiledString)
