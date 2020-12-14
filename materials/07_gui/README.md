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
   <summary>📺 Modul tkinter</summary>

   #### 🆕 Zaciname!
   1. Importujeme modul `tkinter`
   2. Nejprve vytvorime instanci tridy `Tk` jako objekt `gui`
   3. Vytvorime widget se stitkem `my_window`
   4. Pomoci metody `pack()` nastavime zobrazeni widgetu (defaultni)
   5. Pojmenujeme okno s metodou `wm_title()`
   6. Vykreslime okno s `mainloop()`

---

<details>
   <summary>👇 Nas zapis 👇</summary>

   #### 📂 calculator.py
   ```python
   from tkinter import *


   gui = Tk()
   gui.wm_title("almost empty window")

   my_window = Label(gui, text="Kalkulacka!")
   my_window.pack()

   gui.mainloop()
   ```

</details>
<!--Konec uvodni sekce-->
</details>

---

<details>
   <summary>🔥 Vice poli </summary>

   #### 💬 Rozdelime 2 pole
   1. Prvni pole pro vystupy `display`
   2. Druhe pole pro vstupy `buttons`

<details>
   <summary>👇 Nas zapis 👇</summary>

   #### 📂 calculator.py
   ```python
   from tkinter import *


   gui = Tk()
   gui.wm_title("calculator window")

   outputs = Label(gui, text= "Display")
   buttons = Label(gui, text="Buttons")

   outputs.grid(row=0, column=0)
   buttons.grid(row=1, column=0)

   gui.mainloop()
   ```
<!--Konec druhe casti-->
</details>

</details>

---

<details>
   <summary>🔘 Vlastni tlacitko</summary>

   #### 👁Definice tlacitk
   1. Definujeme funkci `write_message`, ta vypise string jako vystup
   2. Definujeme tlacitko jako instanci tridy `Button` (`help(Button)`)
   3. Doplnime argument `command`

<details>
   <summary>👇 Nas zapis 👇</summary>

   #### 📂 calculator.py
   ```python
   from tkinter import *


   gui = Tk()
   gui.wm_title("calculator window")


   def write_message():
       outputs = Label(gui, text="Hello, everybody!")
       outputs.pack()


   my_button = Button(gui, text="Click!", command=write_message, fg= "#FFFFFF", bg="#1BF8B0")
   my_button.pack()

   gui.mainloop()
   ```
<!--Konec treti casti-->
</details>

</details>

---

<details>
   <summary>💻 Kombinace vstupu & vystupu</summary>

   #### ⛓ Propojeni
   1. Vytvorime instanci tridy `Entry` pro vstupni pole
   2. Aplikujeme funkci `insert`
   3. Zkombinujeme ve funkce `write_message` pomoci funkce `get`

<details>
   <summary>👇 Nas zapis 👇</summary>

   #### 📂 calculator.py
   ```python
   from tkinter import *


   gui = Tk()
   gui.wm_title("calculator window")

   entry = Entry(gui, width=50)
   entry.pack()
   entry.insert(0, "Enter your name")


   def write_message():
       message = f"Hello, {entry.get()}"
       outputs = Label(gui, text=message)
       outputs.pack()


   my_button = Button(gui, text="Click!", command=write_message, fg= "#FFFFFF", bg="#1BF8B0")
   my_button.pack()

   gui.mainloop()
   ```
<!--Konec ctvrte casti-->
</details>

</details>

---

<details>
   <summary>✌ Funkcni tlacitka</summary>

   #### 🖱 Vytvorime sekci s tlacitky
   1. Definujeme funkci `on_click` s jednim parametrem `number`
   2. Vytvorime tlacitka s argumenty `1`, `2` a `3`
   3. Pouzijeme tzv. _anonymni funkce_ pro spusteni funkci s parametrem.

   #### ❓ Anonymni funkce
   1. Funkce, ktere jsou jednou pouzitelne
   2. Nemaji jmeno, neukladame jejich definice
   3. Intepret je provede a zahodi
   ```python
   vyraz = lambda cislo: cislo**2
   print(vyraz(4))
   ```
   **Varianta** bez argumentu:
   ```python
   def add_val(num):
       return num + 1


   command = lambda: add_val(3)
   print(command())
   ```
   [**🔝 Vyzkousej sam 🔝**](https://repl.it/@JustBraloR/anonymousfunc#main.py)

<details>
   <summary>👇 Nas zapis 👇</summary>

   #### 📂 calculator.py
   ```python
   from tkinter import *


   gui = Tk()
   gui.wm_title("simple calculator")

   entry = Entry(gui, width=35, borderwidth=5)
   entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


   def on_click(number):
       entry.insert(0, number)


   button_1 = Button(gui, text="1", padx=40, pady=20, command=lambda: on_click(1))
   button_2 = Button(gui, text="2", padx=40, pady=20, command=lambda: on_click(2))
   button_3 = Button(gui, text="3", padx=40, pady=20, command=lambda: on_click(3))

   button_1.grid(row=1, column=0)
   button_2.grid(row=1, column=1)
   button_3.grid(row=1, column=2)

   gui.mainloop()
   ```
<!--Konec pate casti-->
</details>

</details>

---

<details>
   <summary>✍ Radny zapis</summary>

   #### 📝 Jak na to
   1. Vyuzijeme tridu `StringVar`, ta slouzi jako promenna pro uchovani hodnot
   2. Ulozena data vypisujeme pomoci `Entry`, argument `textvariable`
   3. Nastavime defaultni text pomoci metody `set` a pomocnou promennou
   4. Funkce ohlasuje `global`, abychom mohli upravovat hodnotu v glob. ramci

<details>
   <summary>👇 Nas zapis 👇</summary>

   #### 📂 calculator.py
   ```python
   from tkinter import *


   gui = Tk()
   gui.wm_title("simple calculator")

   equation = StringVar()
   entry = Entry(gui, width=35, borderwidth=5, textvariable=equation)
   entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
   equation.set("Enter the expression")
   entry = ""


   def on_click(value):
          global entry
          entry += str(value)
          equation.set(entry)


   button_1 = Button(gui, text="1", padx=40, pady=20, command=lambda: on_click(1))
   button_2 = Button(gui, text="2", padx=40, pady=20, command=lambda: on_click(2))
   button_3 = Button(gui, text="3", padx=40, pady=20, command=lambda: on_click(3))

   button_1.grid(row=1, column=0)
   button_2.grid(row=1, column=1)
   button_3.grid(row=1, column=2)

   gui.mainloop()

   ```
<!--Konec seste casti-->
</details>

</details>

---

<details>
   <summary>➕ Aritmeticke operace</summary>
    
   #### 💼 Chybejici operace
   1. Pridame ctvrte tlacitko, pro scitani `+`
   2. Pridame prvni tlacitko ve druhe rade pro `=`
   3. Pridame funkci `equal`, ktera vyhodnoti obsah `entry`
   4. Funkce `equal` umi pracovat jak s cisly, tak s symboly (`eval`)

<details>
   <summary>👇 Nas zapis 👇</summary>

   #### 📂 calculator.py
   ```python
   from tkinter import *


   gui = Tk()
   gui.wm_title("simple calculator")

   equation = StringVar()
   entry = Entry(gui, width=35, borderwidth=5, textvariable=equation)
   entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
   equation.set("Enter the expression")
   entry = ""


   def on_click(value):
       global entry
       entry += str(value)
       equation.set(entry)


   def equal():
       global entry
       total = str(eval(entry))
       equation.set(total)
       expression = ""


   button_1 = Button(gui, text="1", command=lambda: on_click(1))
   button_2 = Button(gui, text="2", command=lambda: on_click(2))
   button_3 = Button(gui, text="3", command=lambda: on_click(3))
   button_add = Button(gui, text="+", command=lambda: on_click("+"))
   button_eql = Button(gui, text="=", command=equal)

   button_1.grid(row=1, column=0)
   button_2.grid(row=1, column=1)
   button_3.grid(row=1, column=2)
   button_add.grid(row=1, column=3)
   button_eql.grid(row=2, column=0)

   gui.mainloop()
   ```

<!--Konec sedme casti-->
</details>

</details>

---

<details>
   <summary>🗜 Doplnime</summary>

   #### ✍ Opakovani matka...
   Podle predchozich instrukci doplnime zbytek kalkulacky

<details>
   <summary>👇 Nas zapis 👇</summary>

   #### 📂 calculator.py
   ```python
   from tkinter import *


   gui = Tk()
   gui.wm_title("simple calculator")

   equation = StringVar()
   entry = Entry(gui, width=35, borderwidth=5, textvariable=equation)
   entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
   equation.set("Enter the expression")
   entry = ""


   def on_click(value):
       global entry
       entry += str(value)
       equation.set(entry)


   def equal():
       global entry
       total = str(eval(entry))
       equation.set(total)
       expression = ""


   def clear():
       global entry
       entry = ""
       equation.set("")


   button_1 = Button(gui, text="1", padx=40, pady=20, command=lambda: on_click(1))
   button_2 = Button(gui, text="2", padx=40, pady=20, command=lambda: on_click(2))
   button_3 = Button(gui, text="3", padx=40, pady=20, command=lambda: on_click(3))
   button_add = Button(gui, text="+", padx=40, pady=20, command=lambda: on_click("+"))

   button_4 = Button(gui, text="4", padx=40, pady=20, command=lambda: on_click(4))
   button_5 = Button(gui, text="5", padx=40, pady=20, command=lambda: on_click(5))
   button_6 = Button(gui, text="6", padx=40, pady=20, command=lambda: on_click(6))
   button_sub = Button(gui, text="-", padx=40, pady=20, command=lambda: on_click("-"))

   button_7 = Button(gui, text="7", padx=40, pady=20, command=lambda: on_click(7))
   button_8 = Button(gui, text="8", padx=40, pady=20, command=lambda: on_click(8))
   button_9 = Button(gui, text="9", padx=40, pady=20, command=lambda: on_click(9))
   button_mul = Button(gui, text="*", padx=40, pady=20, command=lambda: on_click("*"))

   button_0 = Button(gui, text="0", padx=40, pady=20, command=lambda: on_click(0))
   button_div = Button(gui, text="/", padx=40, pady=20, command=lambda: on_click("/"))
   button_cls = Button(gui, text="CE", padx=26, pady=20, command=clear)
   button_eql = Button(gui, text="=", padx=30, pady=20, command=equal)

   button_1.grid(row=1, column=0)
   button_2.grid(row=1, column=1)
   button_3.grid(row=1, column=2)
   button_add.grid(row=1, column=3)

   button_4.grid(row=2, column=0)
   button_5.grid(row=2, column=1)
   button_6.grid(row=2, column=2)
   button_sub.grid(row=2, column=3)

   button_7.grid(row=3, column=0)
   button_8.grid(row=3, column=1)
   button_9.grid(row=3, column=2)
   button_mul.grid(row=3, column=3)

   button_0.grid(row=4, column=0)
   button_div.grid(row=4, column=1)
   button_cls.grid(row=4, column=2)
   button_eql.grid(row=4, column=3)

   gui.mainloop()
   ```
</details>

</details>

---

➡ [Pokracovat k dalsi casti]()

