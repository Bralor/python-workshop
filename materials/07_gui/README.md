➡ [vratit se k seste casti](https://github.com/Bralor/python-workshop/tree/master/materials/06_networking)

<p align="center">
  <img alt="engeto-logo" width="100px" src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" />
</p>

## 7⃣ Python workshop
### 🗒  Obsah lekce
1. Uzitecne odkazy
2. Ukazka ulohy
3. Modul tkinter
4. Uvodni cast
---

<details>
  <summary>☝  Uzitecne odkazy</summary>

  #### 🗒 Dulezite odkazy
  - [Python, dokumentace zabudovanych funkci](https://docs.python.org/3/library/functions.html)
  - [Modul tkinter](https://docs.python.org/3/library/tkinter.html)

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
   <summary>📺 Uvodni sekce</summary>

   #### 🆕 Zaciname!
   1. Z modulu `tkinter` importujeme vsechno
   2. Nejprve vytvorime instanci tridy `Tk`
   3. Nachystame objekt pro nase nove okno `root`
   4. Vytvorime widget se stitkem
   5. Pomoci metody `pack()` nastavime zobrazeni widgetu
   6. Pojmenujeme okno s metodou `wm_title()`
   7. Vykreslime okno s `mainloop()`

----

<details>
   <summary>👇 Nas zapis 👇</summary>
   ```python
   from tkinter import *

   root = Tk()

   my_label = Label(root, text="Kalkulacka!")
   my_label.pack()

   root.wm_title("calculator window")
   root.mainloop()
   ```

</details>

---

