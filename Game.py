#!/bin/env python3

import random
import os

numbers = {1:"uno", 
2:"dos", 
3:"tres", 
4:"cuatro",
5:"cinco",
6:"seis",
7:"siete",
8:"ocho",
9:"nueve",
10:"diez"}

while True:
    answer = 11
    while answer > 10:
        first = random.choice(list(numbers.items()))
        second = random.choice(list(numbers.items()))
        answer = first[0] + second[0]
    answer = numbers[answer]
    possibles = [answer]
    while len(possibles) < 4:
        p = random.choice(list(numbers.items()))
        if p[1] != answer and p[1] not in possibles: possibles.append(p[1])
    random.shuffle(possibles)

    options = {"a":0, "b":1, "c":2, "d":3}

    os.system("clear")
    print()
    print(f"{first[1]} + {second[1]} = ?")
    print()
    print(f"a: {possibles[0]}")
    print(f"b: {possibles[1]}")
    print(f"c: {possibles[2]}")
    print(f"d: {possibles[3]}")
    print()

    guess = input("Enter answer: ")
    print()

    if guess in "abcd": 
        if possibles[options[guess]] == answer:
            print("Correct! Well done on getting the right answer!")
            print()
        else:
            print("Sorry! That's not the correct answer :-(")
            print()
    else:
        print("You didn't enter a, b, c or d!")
        print()
    input()
