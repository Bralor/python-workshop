#!/usr/bin/python3
import os
import random
import figurka


SLOVA = ["obesenec", "autobus", "klavesnice", "nedele"]
slovo = random.choice(SLOVA)
tajenka = len(slovo) * ["_"]
zivoty = 7
hra_probiha = True

while hra_probiha and zivoty > 0:
    os.system("clear")
    print(figurka.hangman[7 - zivoty])
    print(f"TAJENKA: {' '.join(tajenka)}, ZIVOTY: {zivoty}")
    hadani = input("Hadej pismeno nebo cele slovo:").lower()

    if hadani == slovo:
        hra_probiha = False

    elif len(hadani) == 1 and hadani in slovo:
        for index, pismeno in enumerate(slovo):
            if pismeno == hadani:
                tajenka[index] = hadani
        if "_" not in tajenka:
            hra_probiha = False

    else:
        zivoty -= 1

else:
    if not hra_probiha:
        os.system("clear")
        print(f"TAJENKA: {slovo}")
        print("Super! Vitezis, jsi frajer kurzu!")
    else:
        os.system("clear")
        print(figurka.hangman[7 - zivoty])
        print(f"Bohuzel, prohrals. Hledane slovo: *{slovo}*")

