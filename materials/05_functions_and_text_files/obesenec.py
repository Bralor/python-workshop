#!/usr/bin/python3
import os
from random import sample

import figurka


def vyber_slovo(jmeno_souboru: str) -> list:
    with open(jmeno_souboru, mode="r") as txt_soubor:
        return sample(set(txt_soubor.readlines()), 1)


def stav_hry(tajenka: list, zivoty: int) -> None:
    os.system("clear")
    print(figurka.hangman[7 - zivoty])
    print(f"TAJENKA: {' '.join(tajenka)}, ZIVOTY: {zivoty}")


def zkontroluj_tajenku(pismeno, slovo, tajenka) -> bool:
    for index, pismeno in enumerate(slovo):
        if pismeno == hadani:
            tajenka[index] = hadani
    return False if "_" not in tajenka else True


slovo = vyber_slovo("slova.txt").pop().strip()
tajenka = len(slovo) * ["_"]
zivoty = 7
hra_probiha = True

while hra_probiha and zivoty > 0:
    stav_hry(tajenka, zivoty)
    hadani = input("Hadej pismeno nebo cele slovo:").lower()

    if hadani == slovo:
        hra_probiha = False
    elif len(hadani) == 1 and hadani in slovo:
        hra_probiha = zkontroluj_tajenku(hadani, slovo, tajenka)
    else:
        zivoty -= 1

else:
    if not hra_probiha:
        stav_hry(tajenka, zivoty),
        print("Super! Vitezis, jsi frajer kurzu!")
    else:
        stav_hry(tajenka, zivoty),
        print(f"Bohuzel, prohrals. Hledane slovo: *{slovo}*")

