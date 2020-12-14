➡ [vratit se k sedme casti](https://github.com/Bralor/python-workshop/tree/master/materials/07_gui)

<p align="center">
  <img alt="engeto-logo" width="100px" src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" />
</p>

## 8⃣ Python workshop
### 🗒  Obsah lekce
1. Uzitecne odkazy
2. Ukazka ulohy
3. OOP koncept, obecne
4. OOP, Python
5. Tridni atributy, tridni metody, staticke metody
6. encapsulation
7. abstraction
8. inheritance
9. Polymorphism
10. Dunder methods -> double underscore methods
---

<details>
  <summary>☝  Uzitecne odkazy</summary>

  #### 🗒 Dulezite odkazy
  - [Python, dokumentace zabudovanych funkci](https://docs.python.org/3/library/functions.html)
  - [OOP, priklad](https://www.listendata.com/2019/08/python-object-oriented-programming.html)
  -

</details>

---

<details>
  <summary>⏯  Ukazka ulohy</summary>

  1. ✌  [Stahnete si cely repozitar jako **zip**](https://github.com/Bralor/python-workshop/archive/mh-dev.zip)
  2. 💪 Presunte se ke stazenemu souboru
  3. 🙏 Spustte soubor **materials/06_networking/server.py** v PyCharm
  3. 💅 Spustte soubor **materials/06_networking/client.py** v PyCharm
  4. 🐍 Spustte program pomoci klaves **ctrl+shift+F10**
  5. 🎥 Zkousejte!

</details>

---

<details>
   <summary> 📚 Objektove orientovane programovani</summary>

   #### ☝ K zapamatovani
   1. Jde o zpusob premysleni nad formulaci instrukci
   2. Reprezentace skutecnych objektu (auto, zvire, clovek)
   3. Jde o zpusob organizovani kodu
   Zapis s **funkci**:
   ```python
   def pozdrav_uzivatele():
      return "Ahoj, vsichni!"


    print(pozdrav_uzivatele())
   ```
   Zapis s **tridou**:
   ```python
   class ChatBot:
       def __repr__(self):
           return "Ahoj, vsichni!"


   print(ChatBot())
   ```
   Nejjednodusi formulace:
   ```python
   print("Ahoj, vsichni!")
   ```
<!--Konec prvni casti-->
</details>

---

<details>
   <summary>💻 OOP v Pythonu</summary>

   #### ☝ K zapamatovani
   1. `Auto`-objekt, `dovednost`-funkce (metody v OOP), `atributy`-vlastnosti
   2. [Objekty & tridy](https://www.autodraw.com/share/PXHGARZYD847)
   3. Jmena tridy jsou zapsana jako `CamelCase` (ne `snake_case` jako funkce)
   4. `__init__` je metoda, ktera se spusti jako prvni pri tvorbe instance tridy
   5. `self`, klicovy vyraz, reprezentujici jmeno instance, ktere zatim neexistuje
   6. Parametry `rok_v`, `najeto` a `max_rych` jsou tridni atributy
   7. `rozjed_se` a `zastav_se` jsou tridni metody
   8. `auto_1` je instance tridy `Auto`

   #### 📇 Priklad tridy
   ```python
   class Auto:
       def __init__(self, rok_v, najeto, max_rych):
           self.rok_v = rok_v
           self.najeto = najeto
           self.max_rych = max_rych

       def rozjed_se(self):
           return f"Auto se rozjizdi"

       def zastav_se(self):
           return f"Auto se zastavi"


   auto_1 = Auto(2010, 93_000, 140)
   print(auto_1)
   print(auto_1.rozjed_se())
   print(auto_1.zastav_se())
   ```
<!--Konec druhe casti-->
</details>

---
