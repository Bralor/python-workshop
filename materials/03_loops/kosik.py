#!/usr/bin/python3
""" Lekce #4 - Uvod do programovani, Nakupni kosik """

kosik = {}
ODDELOVAC = "=" * 40
POTRAVINY = {
  "mleko": [30, 5],
  "maso": [100, 1],
  "banan": [30, 10],
  "jogurt": [10, 5],
  "chleb": [20, 5],
  "jablko": [10, 10],
  "pomeranc": [15, 10]
}

print(
"VITEJTE V NASEM VIRTUALNIM OBCHODE".center(40, " "),
end=f"\n{ODDELOVAC}\n"
)
TABULKA = POTRAVINY.copy()

while TABULKA:
    radek_potravina = TABULKA.popitem()
    print(f"POTRAVINA: {radek_potravina[0]},\tCENA: {radek_potravina[1][0]}")
else:
    print(ODDELOVAC)

while (vyber_zbozi := input("VYBERTE ZBOZI: ")) != 'q':

    if vyber_zbozi not in POTRAVINY:
        print(f"{vyber_zbozi} NEMAME V NABIDCE!")

    elif vyber_zbozi not in kosik and POTRAVINY[vyber_zbozi][1] > 0:
        kosik[vyber_zbozi] = [POTRAVINY[vyber_zbozi][0], 1]         # pridam ks
        POTRAVINY[vyber_zbozi][1] = POTRAVINY[vyber_zbozi][1] - 1   # odeberu ks

    elif vyber_zbozi in kosik and POTRAVINY[vyber_zbozi][1] > 0:
        kosik[vyber_zbozi][1] = kosik[vyber_zbozi][1] + 1
        POTRAVINY[vyber_zbozi][1] = POTRAVINY[vyber_zbozi][1] - 1

    elif POTRAVINY[vyber_zbozi][1] == 0:
        print(f"{vyber_zbozi.upper()} JIZ NENI SKLADEM!")

else:
    print("UKONCUJI NAKUP..", ODDELOVAC, sep="\n")
    total = 0

    for potraviny, (cena, kus) in kosik.items():
        print(f"POTRAVINA:{potraviny}\t\t{kus}x {cena}")
        total = total + (cena*kus)
    else:
        print(ODDELOVAC, f"CELKOVA CENA NAKUPU: {total}", sep="\n")

