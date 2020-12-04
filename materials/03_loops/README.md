➡ [vratit se ke druhe casti](https://github.com/Bralor/python-workshop/tree/mh-dev/materials/02_dicts_and_sets)

<p align="center">
  <img alt="engeto-logo" width="100px" src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" />
</p>

## 3⃣ Python workshop
### 🗒 Obsah lekce
1. Uzitecne odkazy
2. Ukazka ulohy
3. Vstupni data
4. Uvodni vypisovani
5. While cyklus
6. Nekonecna smycka
7. Preskocit/pokracovat ohlaseni
8. Walrus operator
9. For cyklus
---

<details>
  <summary>☝ Uzitecne odkazy</summary>

  #### 🗒 Dulezite odkaz
  - [Python Academy, Engeto](https://engeto.com/)
  - [Python Academy, Engeto](https://engeto.com/)
  - [Walrus operator, dokumentace](https://realpython.com/lessons/assignment-expressions/)

</details>

---

<details>
  <summary>⏯  Ukazka ulohy</summary>

  1. ✌  [Stahnete si cely repozitar jako **zip**](https://github.com/Bralor/python-workshop/archive/mh-dev.zip)
  2. 💪 Presunte se ke stazenemu souboru
  3. 🙏 Spustte soubor **materials/03_loops/kosik.py** v PyCharm
  4. 🐍 Spustte program pomoci klaves **ctrl+shift+F10**
  5. 🎥 Zkousejte!

</details>

---

<details>
  <summary>📥 Vstupni data</summary>

  #### 🔰 Pracovni promenne
  ```python
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
  ```

</details>

---

<details>
  <summary>📖 Uvodni vypisovani</summary>

<details>
  <summary>🗣  Pozdrav + vypis promennych</summary>

  #### 🗄 Pozdrav a oddelovac
  ```python
  print(
    "VITEJTE V NASEM VIRTUALNIM OBCHODE".center(40, " "),
    end=f"\n{ODDELOVAC}\n",
  )
  ```

  #### 🛍 Vypis dostupneho zbozi
  ```python
  print(
    POTRAVINY, end=f"\n{ODDELOVAC}\n"
  )
  ```

  #### 🛃 Zkombinujeme oboji
  ```python
  print(
    "VITEJTE V NASEM VIRTUALNIM OBCHODE".center(40, " "),
    POTRAVINY,
    sep=f"\n{ODDELOVAC}\n",
    end=f"\n{ODDELOVAC}\n"
  )
  ```

</details>

<details>
  <summary>🛒 Pridavame zbozi</summary>

  #### 👨 Vyber potraviny
  ```python
  vyber_1 = input("VYBERTE ZBOZI: ")
  ```

  #### 🔚 Prevedeni do kosiku
  ```python
  kosik[vyber_1] = POTRAVINY[vyber_1][0]
  ```

  #### 💲 Vypocet ceny
  Pomuzeme se zabudovanou funkci `sum`:
  ```python
  print(f"CELKEM: {sum(kosik.values())} CZK")
  ```
  **Doplnime pro 4 potraviny**

</details>

</details>

---

<details>
  <summary>♻ While cyklus</summary>

<details>
  <summary>❔Jak jej pozname </summary>

  #### 🔑 Klicove znaky
  1. `while`
  2. podminka
  3. ukoncujici dvojtecka
  4. odsazeni + serie instrukci
  ```python
  while podminka:
    # pokud je podminka True, proved TOTO
  # pokud je podminka False, proved TOTO
  ```

</details>

<details>
  <summary>⏯  Ukazka</summary>

  #### ❗Priklad
  ```python
  x = 0

  while x < 10:
    print(f"{x=}; {x}<10, v poradku!")
    x = x + 1

  print(f"{x=}; {x}=10, podminka neni pravdiva, pokracuje kod pod smyckou!")
  ```
  [**Odkaz**](https://repl.it/@JustBraloR/whileloopexample#main.py) pro spusteni

</details>

<details>
  <summary>🔁 Upravime nas zapis</summary>

  #### ✌ Druhy pokus
  Stavajici kod prepiseme pomoci smycky `while`:
  ```python
  while len(kosik) < 4:
      vyber_zbozi = input(f"VYBERTE ZBOZI: ")
      kosik[vyber_zbozi] = POTRAVINY[vyber_zbozi][0]
  ```

  #### 🤷 Doplnime soucet
  Muzu pokracovat primo pod smyckou nebo pouzit `else`:
  ```python
  else:
    print(
      "KOSIK JE PLNY, UKONCUJI..",
      kosik,
      f"CENA CELKEM: {sum(kosik.values())} CZK",
      sep=f"\n{ODDELOVAC}\n",
      end=f"\n{ODDELOVAC}\n"
    )
  ```

</details>

</details>

---

<details>
  <summary>⚠ Nekonecna smycka</summary>

<details>
  <summary>❓ Jen ctyri produkty</summary>

  #### ☝ Spravna podminka
  Nechceme uzivatele omezit jen na 4 produkty

  #### 💁 Nekonecna smycka
  Podminku v hlavicce cyklu muzeme napsat i nasledovne:
  ```python
  x = 0

  while x < 10:
      print(f"x={x}; {x}<10, v poradku!")
  ```
  [**Odkaz**](https://repl.it/@JustBraloR/infiniteloop#main.py) pro spusteni

  **Pro ukonceni nekonecne smycky Ctrl+C**

  #### ⁉ Je to vhodne
  Neumyslne zapis je samozrejme nezadouci. Ale muzeme jej spravit:
  ```python
  cislo = 1
  prepinac = True

  while prepinac:
      cislo = cislo * 2
      kontrola = input("PRO UKONCENI NAPIS 'q': ").lower()

      if kontrola == "q":
              prepinac = False
      else:
              print(cislo)
  ```
  [**Odkaz**](https://repl.it/@JustBraloR/infiniteloopcorrect#main.py) pro spusteni

<p align="center">
  <img src="https://media.giphy.com/media/qVVVfmHDMBZug/source.gif" width="300" height="300">
</p>

  #### ⏪ Prepiseme nasi podminku v cyklu
  ```python
  pokracovat = True

  while pokracovat:
      vyber_zbozi = input(f"VYBERTE ZBOZI: ")

      if vyber_zbozi.lower() == 'q':
        pokracovat = False
      else:
        kosik[vyber_zbozi] = POTRAVINY[vyber_zbozi][0]

  else:
    print(
      "KOSIK JE PLNY, UKONCUJI..",
      kosik,
      f"CENA CELKEM: {sum(kosik.values())} CZK",
      sep=f"\n{ODDELOVAC}\n",
      end=f"\n{ODDELOVAC}\n"
    )
  ```

</details>

<details>
  <summary>⛔ Chybne jmeno zbozi</summary>

  #### 🤦 Chybu udela kazdy
  Pokud se uzivatel splete, chceme ho upozornit:
  ```python
  if vyber_zbozi.lower() == "q":
      pokracovat = False
  elif vyber_zbozi not in POTRAVINY.keys():
      print(f"*{vyber_zbozi}* BOHUZEL NEMAME SKLADEM!")
  else:
      kosik[vyber_zbozi] = POTRAVINY[vyber_zbozi][0]
  ```

</details>

<details>
  <summary>🚯 Prehledna nabidka</summary>

  #### ⚒  Pomoci cyklu
  Chceme vypisovat pod sebe pomoci `while` cyklu:
  ```python
  TABULKA = POTRAVINY.copy()

  while TABULKA:
      radek_potravina = TABULKA.popitem()
      print(f"POTRAVINA: {radek_potravina[0]},\tCENA: {radek_potravina[1][0]}")
  ```
  [**Odkaz**](https://repl.it/@JustBraloR/dictmethods5#main.py) pro procviceni metod slovniku

</details>

</details>

---

<details>
  <summary>😑 Preskocit nebo pokracovat</summary>

  #### ⏹ Ohlaseni break
  Pomoci klicoveho vyrazu `break` muzeme cyklus predcasne ukoncit:
  ```python
  cislo = 0
  PANGRAM = "Příliš žluťoučký kůň úpěl ďábelské ódy"

  while cislo < len(PANGRAM):
          pismeno = PANGRAM[cislo]
          if pismeno == "w":
              break
          else:
              print(f"{pismeno=}")
              cislo = cislo + 1

  else:
      print(f"POSLEDNI INDEX {len(PANGRAM[:cislo])}")
  ```
  [**Odkaz**](https://repl.it/@JustBraloR/break#main.py) pro spusteni

  #### 🌀 Ohlaseni continue
  Pomoci klicoveho vyrazu `continue` muzeme v cyklu preskakovat:
  ```python
  cislo = 0
  PANGRAM = "Příliš žluťoučký wkůň úpěl ďábelské ódy"

  while cislo < len(PANGRAM):
          pismeno = PANGRAM[cislo]

          if pismeno != "w":
              print(f"SPRAVNA HODNOTA --> {pismeno=}")
              cislo = cislo + 1
              continue
          else:
              print(f"NESPRAVNA HODNOTA --> {pismeno=}")
              cislo = cislo + 1

  else:
      print(f"POSLEDNI INDEX {len(PANGRAM[:cislo])}")
  ```
  [**Odkaz**](https://repl.it/@JustBraloR/continue#main.py) pro spusteni

</details>

---

<details>
  <summary>🚼 Walrus operator</summary>

  #### 📜 Prirazovaci operator 
  Patri mezi novejsi vyrazy (Python3.8+)

  #### 👷 Jak jej pouzivat
  ```python
  # Jednoduchy zapis
  jmeno = "Matous"
  print(jmeno)
  print(jmeno_2 := "Lukas")

  # Podminkovy zapis
  JMENA = {"Matous", "Lukas", "Jan", "Marek"}
  if (n := len(JMENA)) > 3:
      print(f"Set je prilis dlouhy ({n} udaju, ocekavam <= 3)")

  # While cyklus
  while (jmeno := input("NAPIS NECO: ")) != "":
      print(f"NECO: {jmeno}")
  else:
      print("NIC SI NENAPSAL!:P")
  ```
  [**Odkaz**](https://repl.it/@JustBraloR/assignmentoperator#main.py) pro spusteni

  #### 🔂 Aplikujeme v uloze
  Pouziti prirazovaciho operatoru v nasi uloze:
  ```python
  while (vyber_zbozi := input("VYBERTE ZBOZI: ")) != 'q':
      if vyber_zbozi not in POTRAVINY.keys():
          print(f"*{vyber_zbozi}* NEMAME SKLADEM!")
      else:
          kosik[vyber_zbozi] = POTRAVINY[vyber_zbozi][0]
  ```

</details>

---

<details>
  <summary>🔁 For cyklus</summary>

<details>
  <summary>📜 Obecny zapis</summary>

  #### ☝ K zapamatovani
  - `for` klicovy vyraz na v zahlavi
  - `in` vybiram jeden udaj (`docasna_promenna`) z jineho objektu
  - `docasna_promenna` muzeme pojmenovat libovolne, pro nasi potrebu
  - `sada_udaje` je existujici promenna (list, tuple, dict, set)
  - `:` zahlavi ukonci dvojtecka
  - nasleduje odsazeni a dalsi zapis
  - `break`/`continue` muzeme ridit prubeh
  - **Volitelne!** Doplneni `else` vetve

  #### ❓ Jak vypada for loop
  **Obecne:**
  ```python
  for docasna_promenna in sada_udaju:
      # odsazeny zapis ve smycce
  ```
  **Priklad:**
  ```python
  JMENA = ["Helmut", "Helga", "Harold", "Hammet", "Hetfield"]

  for jmeno in JMENA:
      print(f"{jmeno=}")
  ```
  [**Odkaz**](https://repl.it/@JustBraloR/forloop#main.py) pro spusteni

  **Priklad s else:**
  ```python
  pismena = ["a", "b", "c", "d", "e", "g"]
  for pismeno in pismena:
      if pismeno == "g":
          print("Mam hodnotu -> G")
          break
  else:
      print("Neni tu zadne G")
  ```
  [**Odkaz**](https://repl.it/@JustBraloR/forelseloop#main.py) pro spusteni

</details>

<details>
  <summary>💸 Cena od kusu</summary>

  #### 🥅 Nas cil
  1. Nyni ukladam do kosiku `"potravina": castka`
  2. Pokud v kosiku nemam potravinu vlozime `"potravina": [castka, kus=1]`
  3. Nezapomeneme odecist ze slovniku `POTRAVINY` 1 kus
  4. Pokud v kosiku potravinu jiz mam: `"potravina": [castka, kus + 1]`
  5. Opet odecteme 1 kus z `POTRAVINY`
  6. Pokud konkretni potravina nebude skladem nepridavame, pouze vypiseme zpravu
  ```python
  # body 1-3
  elif vyber_zbozi not in kosik and POTRAVINY[vyber_zbozi][1] > 0:
      kosik[vyber_zbozi] = [POTRAVINY[vyber_zbozi][0], 1]         # pridam ks
      POTRAVINY[vyber_zbozi][1] = POTRAVINY[vyber_zbozi][1] - 1   # odeberu ks

  # body 4-5
  elif vyber_zbozi in kosik and POTRAVINY[vyber_zbozi][1] > 0:
      kosik[vyber_zbozi][1] = kosik[vyber_zbozi][1] + 1
      POTRAVINY[vyber_zbozi][1] = POTRAVINY[vyber_zbozi][1] - 1

  # bod 6
  elif POTRAVINY[vyber_zbozi][1] == 0:
      print(f"{vyber_zbozi.upper()} JIZ NENI SKLADEM!")
  ```

</details>

<details>
  <summary>📄 Vypis obsahu a celkove ceny</summary>

  #### 🥅 Nas cil
  1. Projit promennou `kosik`
  2. Vypisovat potravinu, kusy, cenu
  3. Inkrementovat celkovou cenu kazdou iteraci
  ```python
  else:
      print("UKONCUJI NAKUP..", ODDELOVAC, sep="\n")
      total = 0

      for potraviny, (cena, kus) in kosik.items():
          print(f"POTRAVINA:{potraviny}\t\t{kus}x {cena}")
          total = total + (cena*kus)
      else:
          print(ODDELOVAC, f"CELKOVA CENA NAKUPU: {total}", sep="\n")
  ```


</details>

</details>

---

➡ [pokracovat k dalsi casti]()

