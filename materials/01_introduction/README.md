➡ [vratit se na uvod lekci](https://github.com/Bralor/python-workshop/tree/mh-dev)

<p align="center">
  <img alt="engeto-logo" width="100px" src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" />
</p>

## 1⃣ Python workshop
### 🗒  Obsah lekce
1. Uzitecne odkazy
2. Ukazka ulohy
3. Pracovni prostredi
4. Ciselne a textove hodnoty
5. Promenne
6. Kontejnerove datove typy
7. Vstupy & vystupy
8. Boolean & logicke operatory
9. Logicke operatory
10. Podminkovy zapis, obecne
11. Podminkovy zapis, upravujeme program

---

<details>
  <summary>☝  Uzitecne odkazy</summary>

  #### 🗒 Dulezite odkazy
  - [Repl.it](https://repl.it/)
  - [Engeto.com](https://engeto.com/cs/)
  - [Python Academy, Git](https://engeto.com/cs/kurz/git-zaklady-pro-uzivatele/lekce)
  - [Python Academy, zaciname!](https://engeto.com/cs/kurz/python-academy/studium/SpmtH-mVRY6zPL9alhruMQ/home-set-up/basics-of-command-line)
  - [Python, dokumentace zabudovanych funkci](https://docs.python.org/3/library/functions.html)

</details>

---

<details>
  <summary>⏯  Ukazka ulohy</summary>

  1. ✌  [Stahnete si cely repozitar jako **zip**](https://github.com/Bralor/python-workshop/archive/mh-dev.zip)
  2. 💪 Presunte se ke stazenemu souboru
  3. 🙏 Spustte soubor **materials/01_introduction/destinatio.py** v PyCharm
  4. 🐍 Spustte program pomoci klaves **ctrl+shift+F10**
  5. 🎥 Zkousejte!

</details>

---

<details>
  <summary>🔨 Pracovni prostredi</summary>

  #### ⚒ Jak pracovat s Pythonem
  1. ⏯ [PyCharm community edition](https://www.jetbrains.com/help/pycharm/quick-start-guide.html)
  2. ➕ Klikneme na novy projekt
  3. 🏘 Vybereme adresar **python_akademie**, vybere interpreta Pythonu (3.8+)
  4. 📁 Vytvorime adresar pro druhou lekci **lekce02**
  5. 🐍 Vytvorime novy soubor **prvni_pokus** (pripona `.py`)
  6. ✏  Na prvni radek napiseme `print("Muj prvni lokalni Python soubor!")`
  7. 🏃 Klikneme pravym tlacitkem mysi na zalozku se jmenem souboru a spustime ho
  8. 👇 Na spodu se vysune karta s dokoncenym interpretovanim naseho zapisu.

</details>

---

<details>
  <summary>🔜 Ciselne a textove hodnoty</summary>

<details>
  <summary>🔢 Cela cisla</summary>

  #### ☝ K zapamatovani (integers)
  ```python
  100 + 200  # 300
  300 - 100  # 200
  type(1234) # overeni
  ```
---

</details>

<details>
  <summary>💲 Desetinna cisla</summary>

  #### ☝  K zapamatovani (floats)
  **Pozor!** Desetinnym oddelovacem je tecka. Carka slouzi k jinym ucelum.
  ```python
  0.1 + 0.3  # 0.4
  type(0.4)  # overeni
  ```
  **Plovouci radova carka** nektera desetinna cisla nemaji odpovidajici
  binarni tvar. Proto jsou ulozena jako priblizne hodnoty.
  ```python
  0.1 + 0.2  # 0.30000000000000004
  type(0.3)  # overeni
  ```
---

</details>

<details>
  <summary>💹 Aritmeticke operace</summary>

  #### ☝ K zapamatovani
  ```python
  10 + 5    # 15
  10 - 5    # 5
  10 * 5    # 50
  10 / 5    # 2.0 (?)
  10 // 3   # celociselne deleni
  10 % 3    # ziskani zbytku po deleni
  10 ** 3   # umocnovani
  ```
---

</details>

<details>
  <summary>🔡 Textove hodnoty</summary>

  #### 🆎 Retezce(strings)
  Ruzne dlouhe uskupeni znaku (cisla, pismena, specialni symboly), ohranicene
  uvozovkami:
  1. `'Matous'` jednoduche uvozovky
  2. `"Matous"` dvojite uvozovky
  3. `"""Matous"""` trojite uvozovky (take `'''Matous'''`)

  ```python
  "Matous Holinka"  # <class 'str'>
  '1234566789'      # <class 'str'>
  "!@#$%%^&*"       # <class 'str'>
  '''Matous
  Holinka'''        # 'Matous\nHolinka'
  ```
---

</details>

<details>
  <summary>🔁 Prevadeni</summary>

  #### 🔀 Z retezce na cislo
  ```python
  2 + 2         # 4
  "2" + "2"     # '22'
  type("2")          # <class 'str'>
  type(int("2"))     # <class 'int'>
  ```
  **Nektere datove typy neni mozne prevest!**

</details>

</details>

---

<details>
  <summary>📦 Promenne</summary>

  #### ☝ K zapamatovani
  - promenne jsou v podstate symbolicke odkazy
  - v pameti odkazuji na konkretni objekt
  - potrebne pokud chceme hodnotu opakovane pouzivat
  - v Pythonu muzeme prepisovat typ hodnoty

  #### 📺 Zapis
  ```python
  jmeno_promenne = "hodnota_promenne"
  ```
  **Pozor!** Jista [pravidla](https://easycodebook.com/python-variable-names-and-naming-rules/)
  musime dodrzet i pri vytvareni jmen promennych.

  ```python
  MESTO = 'Praha'     # <class 'str'>
  MNOZSTVI = 2        # <class 'int'>
  CENA = 1000.5       # <class 'float'>
  ```

</details>

---

<details>
  <summary>📬 Kontejnerove datove typy</summary>

<details>
  <summary>📑 Seznam</summary>

  #### ☝ K zapamatovani (list)
  - tvoreny hranatymi zavorkami
  - udaje oddelene _carkou_ (ucel carky je tedy datovy oddelovac)
  - muzeme pridavat a odebirat udaje (_zmenitelna_ posloupnost)
  - udaje maji dane _poradi_
  - muze obsahovat retezec, cela cisla, desetinna cisla i jine seznamy
  - muzeme _indexovat_

  #### ❓ Jak vypada seznam
  ```python
  jmeno_seznamu = ["udaj_1", "udaj_2", "udaj_3", "udaj_4"]
  ```

  #### 🔝 Nas prvni seznam
  **Konstanta** obsahuje mesta, ktere budeme pouzivat v prvni uloze:
  ```python
  MESTA = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
  type(MESTA)
  ```
  Indexovani umoznuje najit hodnotu pomoci jejiho indexu:
  ```python
  MESTA[0]      # vrati udaj s indexem 0 (prvni hodnotu v zavorkach)
  MESTA[-1]     # vrati udaj s indexem -1 (posledni hodnota)
  MESTA[1]      # vrati udaj s indexem 1 (druha hodnota)
  ```
---

</details>

<details>
  <summary> 🤕 Ntice</summary>

  #### ☝ K zapamatovani (tuple)
  - tvoreny kulatymi zavorkami
  - udaje oddelene _carkou_ (ucel carky je tedy datovy oddelovac)
  - **nemuzeme** pridavat a odebirat udaje (_nezmenitelna_ posloupnost)
  - udaje maji dane _poradi_
  - muze obsahovat retezec, cela cisla, desetinna cisla, seznamy a ntice
  - muzeme _indexovat_

  #### ❓ Jak vypada ntice
  ```python
  jmeno_tuplu = ("udaj_1", "udaj_2", "udaj_3", "udaj_4")
  ```

  #### 🔝 Nas prvni tupl
  **Konstanta** obsahuje ceny imaginarniho jizdneho:
  ```python
  CENY = (150, 200, 120, 120, 100, 180)
  type(CENY)
  ```
  Indexovani umoznuje najit hodnotu pomoci jejiho indexu:
  ```python
  CENY[0]       # vrati udaj s indexem 0 (prvni hodnotu v zavorkach)
  CENY[-1]      # vrati udaj s indexem -1 (posledni hodnota)
  CENY[1]       # vrati udaj s indexem 1 (druha hodnota)
  ```

</details>

</details>

---


<details>
  <summary>🗣 Vstupy & vystupy</summary>

<details>
  <summary>👋 Nejprve uvod</summary>

  #### 🛠 S cim budeme pracovat
  Nejprve potrebujeme promenne:
  ```python
  #!/usr/bin/python3
  """Lekce #01 - Uvod do programovani, Destinatio"""

  AKT_ROK = 2020
  SLEVY = ("Olomouc", "Svitavy")
  CENY = (150, 200, 120, 120, 100, 180)
  ODDELOVAC = "==================================="
  MESTA = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
  ```

  #### 🖨  Vypiseme pozdrav
  Pomoci zabudovane funkce `print`, pozdravime uzivatele:
  ```python
  print("VITEJTE U NASI APLIKACE DESTINATIO!")  # I. varianta

  pozdrav = "VITEJTE U NASI APLIKACE DESTINATIO!"
  print(pozdrav)  # II. varianta
  ```

  #### 🖌 Oddelime text
  ```python
  print("VITEJTE U NASI APLIKACE DESTINATIO!")  # I. varianta
  print(ODDELOVAC)
  ```

  #### 📋 Zobrazime nabidku
  Nakopirujeme nabidku a opet oddelime:
  ```python
  print(
  """
  1 - Praha   | 150
  2 - Viden   | 200
  3 - Olomouc | 120
  4 - Svitavy | 120
  5 - Zlin    | 100
  6 - Ostrava | 180
  """
  )
  print(ODDELOVAC)
  ```
---

</details>

<details>
  <summary>✍ Zapiseme udaje</summary>

  #### ☺ Jak ulozit vstupy
  Pomoci dalsi funkce, `input`, muzeme udaje do naseho programu ulozit:
  ```python
  jmeno = input("ZAPIS SVOJE JMENO: ")
  print(jmeno, type(jmeno))
  ```

  #### ☝ Jake udaje
  1. vyber lokality
  2. jmeno
  3. prijmeni
  4. rok narozeni
  5. e-mail
  6. heslo

  ```python
  cislo_lokality = int(input("VYBERTE CISLO LOKALITY: "))
  jmeno = input("JMENO: ")
  prijmeni = input("PRIJMENI: ")
  rok_narozeni = int(input("ROK NAROZENI: "))
  email = input("EMAIL: ")
  heslo = input("HESLO: ")
  print(ODDELOVAC)
  ```
---
</details>

<details>
  <summary>📤 Propojeni vstupu a hodnot</summary>

  #### 🕹 Vyber lokalit
  Chceme propojit promennou `cislo_lokality` a nase `MESTA`:
  ```python
  MESTA = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
  MESTA[0]  # "Praha"
  MESTA[1]  # "Viden"

  vyber_1 = 0
  vyber_2 = 1
  ```

  #### ➕ Zapojeni vstupu
  ```python
  destinace = MESTA[cislo_lokality - 1]
  cena = CENY[cislo_lokality - 1]
  ```

</details>

<details>
  <summary>👥 Vystup programu</summary>

  #### 😧 Spojovani(concatenation)
  Ve funkci `print` budeme kombinovat retezce a hodnoty z promennych:
  ```python
  print("DESTINACE: " + destinace)
  ```

  #### 📎 Vice vystupu
  Funkce `print` umoznuje vypsat vice udaju:
  ```python
  print("DEKUJI, ", jmeno, "JIZDENKU POSLEME NA EMAIL: ", email)
  ```

  #### ⏩ F-string formatovani
  ```python
  print(f"CENA(cil: {destinace}): {cena}")
  ```

</details>

</details>

---

<details>
  <summary> 👌 Boolean & logicke operatory</summary>

<details>
  <summary>📘 Datovy typ boolean</summary>

  #### ☝ K zapamatovani (boolean)
  - specialni datovy typ spadajici pod _integer_
  - ciselne hodnoty **1** a **0**
  - hodnoty **True** a **False**
  - pomahaji resit, jestli je podminka/metoda pravdiva nebo neni

  #### ❓ Jak vypada boolean
  ```python
  jmeno_promenne = True
  ```

  #### 🔎 Co je vsechno pravda (v Pythonu)
  Funkce `bool` nam pomuze zjistovat, co je ci neni pravdive:
  ```python
  bool(1 < 3)   # True
  bool(1 < -3)  # False
  ```
  **Pozor!** Funkce `bool` muze vratit boolean hodnotu i u hodnot, u kterych
  bychom je necekali:
  ```python
  bool(2)           # True
  bool("Matous")    # True
  bool("")          # False
  bool(" ")         # True
  bool([])          # False
  bool([" "])       # True
  ```

</details>

<details>
  <summary>📍 Logicke operatory</summary>
  
  #### 💻 Vypis logickych operatoru
  S boolean hodnotami souvisi pouziti logickych operatoru:
  1. `and`
  2. `or`
  3. `not`
  ```python
  bool(True and True)       # True
  bool(True and False)      # False
  bool(False and False)     # False
  bool(not True)            # False

  bool(True or True)        # True
  bool(True or False)       # True
  bool(False or True)       # True
  bool(False or False)      # False
  ```
</details>

</details>

---

<details>
  <summary>👉 Podminkovy zapis</summary>

<details>
  <summary>⚙  Obecny zapis</summary>

  #### ☝ K zapamatovani (conditional statement)
  1. `if` klicovy vyraz
  2. `bool()` overovany vyraz
  3. `:` zahlavi zakoncene dvojteckou
  4. odsazeny odstavec instrukci
  5. `else` podminkovou vetev
  6. `elif` podminkovou vetev

  #### 🎨 Jak vypada podminkovy zapis
  ```python
  X = 10_000  # u 'int' muzeme oddelit cislice podtrzitkem
  Y = 15_000

  if X < Y:
      print("Ano, to je pravda!")
  else:
      print("Ne, toto neni pravda!")
  ```
  **control-flow** ve vzoru vyse je jednoduchy podminkovy zapis slozeny
  z dvou moznych scenaru.

---

</details>

<details>
  <summary>🔢 Platne cislo lokality</summary>

  #### 📺 Prvni podminka
  ```python
  if cislo_lokality > 0 or cislo_lokality < 6:
    # pocitame cenu
  else:
    # ukoncime
  ```

  #### ↔ Delka objektu
  Pomoci funkce `len` muzeme zjistit delku objektu:
  ```python
  PISMENA = ["a", "b", "c"]; len(PISMENA) # 3
  JMENO = "Matous"; len(JMENO)            # 6
  ```

  #### ⏹ Ukonceni programu
  Pro ukonceni beziciho programu mame tyto moznosti:
  1. `exit()`
  2. `quit()`
  3. `sys.exit()`/`os._exit()`

  **Pozor!** `exit`/`quit` funkce ukazuji na stejny objekt
  **Varianta 3** vice se dozvime az v lekci o modulech v Pythonu

  #### 🔁 Opravime prvni podminku
  ```python
  cislo_lokality = int(input("VYBERTE CISLO LOKALITY: "))

  if 0 < cislo_lokality < len(MESTA):
      destinace = MESTA[cislo_lokality - 1]
      cena = CENY[cislo_lokality - 1]
      print(f"DESTINACE: {destinace}")
      print(ODDELOVAC)
  else:
      print("VAMI VYBRANE CISLO NENI V NABIDCE, UKONCUJI..")
      quit()
  ```
---

</details>

<details>
  <summary>💰 Vypocet ceny po sleve</summary>

  #### 💁 Overeni clenstvi
  V podstate se ptame, jestli je nejaky udaj soucasti konkretni sekvence:
  ```python
  JMENA = ("Marek", "Lukas", "Jan")

  bool("Marek" in JMENA)  # True
  bool("Tomas" in JMENA)  # False
  ```

  #### 🆕 Nova cena
  Pokud je cilova lokalita mezi zlevnenymi, vypocitej novou cenu:
  ```python
  if destinace in SLEVY:
      cena_po_sleve = 0.75 * cena
      print("ZISKAVATE 25% SLEVU!")
  else:
      cena_po_sleve = cena
  ```
---

</details>

<details>
  <summary>📛 Spravne jmeno a prijmeni</summary>

  #### 🥅 Nas cil
  Potrebujeme overit, jestli promenne `jmeno` a `prijmeni` obsahuji pouze
  symboly pismen.

  #### 🖱  Metody retezcu
  Datove typy maji uzitecne pomucky pro efektivnejsi praci s nimi:
  1. `isalpha` - vrati `True` pokud jsou vsechny znaky pismena, jinak `False`
  2. `isnumeric` - vrati `True` pokud jsou vsechny znaky cislice, jinak `False`
  ```python
  help(str)  # napoveda pro retezce v ramci interpretu
  ```

  #### 💡 Overeni udaju
  ```python
  jmeno = input("JMENO: ")
  prijmeni = input("PRIJMENI: ")

  if jmeno.isalpha() and prijmeni.isalpha():
      print(f"JMENO: {jmeno}, PRIJMENI: {prijmeni}")
      print(ODDELOVAC)
  else:
      print("JMENO A PRIJMENI MUSI OBSAHOVAT POUZE PISMENA, UKONCUJI..")
      quit()
  ```
---

</details>

<details>
  <summary>👶 Overeni veku uzivatele</summary>

  #### 🥅 Nas cil
  Jen uzivatele starsi 18ti let mohou pouzivat nasi aplikaci. Ostatnim omezime
  pristup.

  #### 🖱 Metody retezcu
  ```python
  vek = int(input("ROK NAROZENI: "))

  if (AKT_ROK - vek) >= 18:
      print("POKRACUJI..")
      print(ODDELOVAC)
  else:
      print("NASE SLUZBY MOHOU VYUZIVAT POUZE OSOBY STARSI 18 LET, UKONCUJI..")
      quit()
  ```
---

</details>

<details>
  <summary>📮 Overeni emailu uzivatele</summary>

  #### 🥅 Nas cil
  Mailovou adresu overime pomoci dvou kriterii:
  1. Obsahuje znak `@`
  2. Obsahuje `.cz` (TLD)

  #### 🏫 Spojeni dvou podminek
  ```python
  email = input("EMAIL: ")

  if "@" in email and ".cz" in email:
      print("EMAIL V PORADKU, POKRACUJI..")
      print(ODDELOVAC)
  else:
      print("NEPODPOROVANY FORMAT EMAILU, UKONCUJI..")
      quit()
  ```

  #### 🔪Cast retezce
  Pokud chceme ziskat jen vyrez z retezce (slicing):
  ```python
  jmeno = "Matous"

  jmeno[0:2]  # jmeno[start:stop] -> prvni 3 pismena
  jmeno[:3]   # jmeno[start:stop] -> prvni 3 pismena
  jmeno[3:]   # jmeno[start:stop] -> bez prvnich 3 pismen
  jmeno[-3:]   # jmeno[start:stop] -> posledni 3 pismena
  ```
  #### 🆕 Upravena podminka
  Overime, ze se `.cz` nachazi na poslednich 3 indexech (pomoci `==`):
  ```python
  email = input("EMAIL: ")

  if "@" in email and email[-3:] == ".cz":
      print("EMAIL V PORADKU, POKRACUJI..")
      print(ODDELOVAC)
  else:
      print("NEPODPOROVANY FORMAT EMAILU, UKONCUJI..")
      quit()
  ```
---

</details>

<details>
  <summary>🛂 Overeni hesla</summary>

  #### 🥅 Nas cil
  Heslo musi splnovat nasledujici kriteria:
  1. Je dlouhe alespon 8 znaku
  2. Obsahuje cislice
  3. Obsahuje pismena

  #### 📏 Delka
  ```python
  heslo = "panpes738";bool(len(heslo) >= 8)
  ```

  #### 🔢 Cislice
  ```python
  heslo = "12345678";heslo.isnumeric()
  ```

  #### 🔡 Pismena
  ```python
  heslo = "abcdefgh";heslo.isalpha()
  ```

  #### 🤼 Zkombinujeme vse
  ```python
  if len(heslo) >= 8 and not heslo.isalpha() and not heslo.isnumeric():
      # True and not False and not False
      # True and True and True -> True
      print("HESLO V PORADKU")
      print(ODDELOVAC)
      print("DESTINACE: " + destinace)
      print("DEKUJEME,", jmeno, "JIZDENKU POSLEME NA EMAIL:", email)
      print(f"CENA (CIL: {destinace}): {cena}")
  else:
      # True and not True and not False
      # True and False and True -> False
      print(
          """TVOJE HESLO JE SPATNE ZADANE:
      1. MUSI OBSAHOVAT ALESPON 8 ZNAKU
      2. MUSI OBSAHOVAT PISMENA
      3. MUSI OBSAHOVAT CISLICE
      """
      )
  ```

</details>

</details>

---

➡ [pokracovat na druhou cast]()

