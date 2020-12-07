➡ [vratit se ke ctvrte casti](https://github.com/Bralor/python-workshop/tree/master/materials/04_importing)

<p align="center">
  <img alt="engeto-logo" width="100px" src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" />
</p>

## 5⃣ Python workshop
### 🗒  Obsah lekce
1. Uzitecne odkazy
2. Ukazka ulohy
3. Funkce, zabudovane
4. Funkce, definovane
5. Textove soubory
6. Name == '\_\_main\_\_'
---

<details>
  <summary>☝  Uzitecne odkazy</summary>

  #### 🗒 Dulezite odkazy
  - [Repl.it](https://repl.it/)
  - [Engeto.com](https://engeto.com/cs/)
  - [Python Academy, Git](https://engeto.com/cs/kurz/git-zaklady-pro-uzivatele/lekce)
  - [Python, dokumentace zabudovanych funkci](https://docs.python.org/3/library/functions.html)
  - [Predpis, if \_\_name\_\_ == '\_\_main\_\_'](https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/)
  - [Python Academy, zaciname!](https://engeto.com/cs/kurz/python-academy/studium/SpmtH-mVRY6zPL9alhruMQ/home-set-up/basics-of-command-line)

</details>

---

<details>
  <summary>⏯  Ukazka ulohy</summary>

  1. ✌  [Stahnete si cely repozitar jako **zip**](https://github.com/Bralor/python-workshop/archive/mh-dev.zip)
  2. 💪 Presunte se ke stazenemu souboru
  3. 🙏 Spustte soubor **materials/05_functions_and_text_files/obesenec.py** v PyCharm
  4. 🐍 Spustte program pomoci klaves **ctrl+shift+F10**
  5. 🎥 Zkousejte!

</details>

---

<details>
  <summary>👼 Funkce, zabudovane</summary>

  #### ☝ K zapamatovani
  - jako uzivatel je nemusim definovat
  - mohu je primo pouzit ( _zavolat_)
  - soupisku vsech najdeme v sekci [odkazy](#dulezite-odkazy)
  - setrime vypisovani
  - zapis je citelnejsi
  - opakovane pouzitelne

  #### ❓ Jak vypada zabudovana funkce
  ```python
  print("Ahoj, vsem!")
  int(input("Zadejte cislo:"))
  ```

</details>

---

<details>
  <summary>🔥 Funkce, uzivatelem definovane</summary>

<details>
  <summary>🤦 Obecne informace</summary>

  #### ☝ K zapamatovani
  - neni soucasti standartni knihovny
  - nejprve definuji, potom pouziju
  - `def` klicovy vyraz v zahlavi definice
  - `jmeno_funkce` nasleduje jmeno funkce, budu potrebovat pri spusteni
  - `parametr1`, `parametr2` v kulate zavorce je parametr funkce (idealne 2)
  - pokud jmeno funkce nestaci, zapisu dokumentaci
  - `return` ohlaseni, pokud chci z funkce vratit nejaky udaj
  - `jmeno_funkce()` spusteni funkce (_volani_)
  - `argument1`, `argument2` skutecne promenne, ktere dosadime do parametru

  #### ❓ Jak vypada zabudovana funkce
  ```python
  def jmeno_funkce(parametr_1, parametr_2):
      """Popis ucelu funkce, pokud jmeno nestaci"""
      pass                              # odsazeny kod
                                        # VOLITELNE: vraceni hodnoty


  jmeno_funkce(argument1, argument2)    # spousteni funkce(volani)
  ```

  **Priklad funkce**
  ```python
  def vypocitej_sumu(cisla):
    """Dokumentace funkce"""
    suma_cisel = 0

    for cislo in cisla:
        suma_cisel = suma_cisel + cislo

    return suma_cisel


  seznam_cisel = [11, 22, 33, 44, 55, 66, 77, 88, 99]
  vysledek = vypocitej_sumu(seznam_cisel)
  print(f"SUMA VSECH CISEL: {vysledek}")
  ```
  [**Odkaz**](https://repl.it/@JustBraloR/functions#main.py) pro spusteni

  **Pozor!** Nas zapis muzeme vylepsit nekolika kroky:
  1. Napovidani datovych typu
  2. Zkraceny zapis
  3. f-string, volani funkce
  4. Idealne pouzit `sum` funkci 😏
---

</details>

<details>
   <summary> ⌚ Aktualni stav hry</summary>

   #### 📔 Prvni funkce
   1. Vytvorime funkci `stav_hry`
   2. Funkce bude mit 2 parametry: `tajenka`, `zivoty`
   3. Funkce bude "cistit" vystup
   4. Kreslit sibenici
   5. Zobrazovat aktualni stav hry
   6. Spustime ji na vhodnych mistech
   ```python
   def stav_hry(tajenka: list, zivoty: int) -> None:
       os.system("clear")
       print(figurka.hangman[7 - zivoty])
       print(f"TAJENKA: {' '.join(tajenka)}, ZIVOTY: {zivoty}")


   stav_hry(tajenka, zivoty)
   ```
</details>

<details>
   <summary> 🏁 Kontrola hracova hadani</summary>

   #### 📔 Druha funkce
   1. Vytvorime funkci `zkontroluj_tajenku`
   2. Funkce bude mit 3 parametry: `pismeno`, `slovo`, `tajenka`
   3. Funkce bude kontrolovat pismeno po pismeno v tajnem slove, prip.
   prepisovat puvodni `tajenka`
   4. Funkce muze ukoncit hru na zaklade nuloveho vyskytu `_` v `tajenka`
   ```python
   def zkontroluj_tajenku(pismeno, slovo, tajenka) -> bool:
       for index, pismeno in enumerate(slovo):
           if pismeno == hadani:
               tajenka[index] = hadani
       return False if "_" not in tajenka else True


   hra_probiha = zkontroluj_tajenku(hadani, slovo, tajenka)
   ```

</details>

</details>

---

<details>
  <summary>⚒ Jak pracovat s textovymi soubory</summary>

  #### ☝ K zapamatovani
  1. Nejprve pouzijeme funkci `open`, abychom otevreli cely soubor
  ```python
  soubor_se_slovy = open()
  ```

  2. Standartne potrebujeme vyplnit pouze prvni dva argumenty:
    - `jmeno_souboru` - i s priponou
    - `mode` - rezim, jak chceme soubor zpracovat ( **r**ead, **w**rite, **a**ppend)
    - `encoding` - volitelne (ruzne soubory, ruzne kodovani). Idealne: `utf8`

  3. Pro nacteni obsahu pouzijeme jednu z metod:
    - `read` - nacteme cely obsah jako `str`
    - `readline` - nacteme pouze prvni radek
    - `readlines` - nacteme jako `list`, obsah rozdelime pomoci `\n`
  ```python
  obsazeny_text = soubor_se_slovy.readlines()
  ```

  4. Nakonec musime otevreny soubor zavrit pomoci metody `close`
  ```python
  soubor_se_slovy = open(jmeno_souboru, mode="r", encoding="utf8")
  obsazeny_text = soubor_se_slovy.read()
  soubor_se_slovy.close()
  ```
---

<details>
  <summary>⚙ Dalsi varianta</summary>

  #### 📀 Kontextovy manazer
  ```python
  with open(jmeno_souboru, mode="r") as txt_file:
      obsazeny_text = txt_file.read()
  ```

  #### 💾 Vlozime do funkce
  1. Vytvorime funkci `vyber_slovo`
  2. Parametrem bude `jmeno_souboru`
  3. Z udaju v souboru udelame nejprve `set` (odstranime pripadne duplicity)
  4. Potom upravime funkci z modulu `random`
  5. Vracime jedine slovo (libovolny datovy typ)
  ```python
  def vyber_slovo(jmeno_souboru: str) -> list:
      with open(jmeno_souboru, mode="r") as txt_soubor:
          return sample(set(txt_soubor.readlines()), 1)


  slovo = vyber_slovo("slova.txt").pop().strip()
  ```

</details>

</details>

---

<details>
   <summary>🆕 Name == main</summary>

   #### 🥅 Motivace
   Po nahrani modulu nechceme spustit cely jeho obsah. Chceme vyuzit jeho
   funkcionalitu jednu po druhe.

   #### ❗ Nevhodna syntaxe
   Pokud bezne spoustime soubor `py` do promenne `__name__` ulozime hodnotu
   jmeno souboru:
   ```python
   def hlavni():
       print("Spoustim hlavni funkci()")
       print("Volani prvni funkce...")
       funkce_1()
       print("Volani druhe funkce...")
       funkce_2()
       print("Volani treti funkce...")
       funkce_3()


   def funkce_1():
       print("Spousteni prvni funkce...")


   def funkce_2():
       print("Spousteni druhe funkce...")


   def funkce_3():
       print("Spousteni treti funkce...")


   hlavni()
   ```
   [**Odkaz**](https://repl.it/@JustBraloR/runningnamemain#main.py) pro spusteni

   **Pozor!** Toto neni zadouci, pokud chceme soubor pouze nahrat. Vyzkousime
   soubor nahrat primo v interpretu.

   #### ✅ Vhodna syntaxe
   Pokud piseme kod do souboru, ktery budeme chtit potencialne pouzivat pozdeji
   (modul), pouzijeme:
   ```python
   if __name__ == "__main__":
       hlavni()
   ```
   Diky takovemu predpisu porad plati: `__name__ == "<jmeno_souboru>"`. Ale
   soucasne pri nahrani z jineho modulu `__name__ == "__main__"`:
   ```python
   if __name__ == "__main__":
       print("Spousteni pres importovani")
       hlavni()
   else:
       print("Naimportovano!")
   ```

</details>

---

