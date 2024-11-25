## Práce se soubory

### Úvod

Python nabízí jednoduchý způsob práce se soubory. Můžeme číst data ze souborů, zapisovat data do souborů a manipulovat se soubory.

### Otevření souboru

Pro otevření souboru použijeme funkci `open()`. Tato funkce přijímá dva argumenty:

* **Název souboru:** Cesta k souboru, který chceme otevřít.
* **Režim:** Určuje, jakým způsobem chceme se souborem pracovat (čtení, zápis, přidávání).

```python
soubor = open("muj_soubor.txt", "r")  # Otevření souboru pro čtení
```

### Relativní a absolutní cesty

* **Absolutní cesta:**  Úplná cesta k souboru, začínající kořenovým adresářem (např. `C:\Users\jmeno\Dokumenty\muj_soubor.txt` na Windows nebo `/home/jmeno/Dokumenty/muj_soubor.txt` na Linuxu).
* **Relativní cesta:** Cesta k souboru vztažená k adresáři, **ze kterého je skript spuštěn**, nikoliv k adresáři, kde je uložen. 

**Příklad:**

Pokud je váš skript uložen v adresáři `/home/jmeno/skripty/muj_skript.py` a vy jej spustíte z adresáře `/home/jmeno/`, pak relativní cesta `skripty/muj_soubor.txt` bude hledat soubor v adresáři `/home/jmeno/skripty/`. 

### Nalezení souboru ve stejné složce

Pro nalezení souboru ve stejné složce jako spuštěný skript můžeme použít následující kód:

```python
from os import path

cesta_k_souboru = path.join(path.dirname(path.realpath(__file__)), "muj_soubor.txt")
soubor = open(cesta_k_souboru, "r")
```

* `path.realpath(__file__)`: Vrátí absolutní cestu k aktuálnímu skriptu.
* `path.dirname(...)`: Vrátí cestu k adresáři, ve kterém se nachází skript.
* `path.join(...)`: Spojí cestu k adresáři s názvem souboru.

### Režimy otevření souboru

* **`r` (read):** Otevře soubor pro čtení.
* **`w` (write):** Otevře soubor pro zápis. Pokud soubor existuje, jeho obsah se smaže. Pokud neexistuje, vytvoří se nový.
* **`a` (append):** Otevře soubor pro přidávání. Data se zapisují na konec souboru.
* **`x` (create):** Vytvoří nový soubor. Pokud soubor již existuje, vyvolá se chyba.
* **`t` (text):** Otevře soubor v textovém režimu (výchozí).
* **`b` (binary):** Otevře soubor v binárním režimu (např. pro obrázky).

### Čtení ze souboru

* **`read()`:** Přečte celý obsah souboru jako řetězec.
* **`readline()`:** Přečte jeden řádek ze souboru.
* **`readlines()`:** Přečte všechny řádky ze souboru a vrátí je jako seznam.

```python
soubor = open("muj_soubor.txt", "r")

obsah = soubor.read()  # Přečtení celého souboru
print(obsah)

soubor.seek(0)  # Nastavení kurzoru na začátek souboru

prvni_radek = soubor.readline()  # Přečtení prvního řádku
print(prvni_radek)

vsechny_radky = soubor.readlines()  # Přečtení všech řádků
print(vsechny_radky)

soubor.close()  # Zavření souboru
```

### Zápis do souboru

* **`write()`:** Zapíše řetězec do souboru.
* **`writelines()`:** Zapíše seznam řetězců do souboru.

```python
soubor = open("muj_soubor.txt", "w")

soubor.write("Toto je první řádek.\n")
soubor.write("Toto je druhý řádek.")

soubor.close()
```

### Uzavření souboru

Po skončení práce se souborem je důležité ho zavřít pomocí metody `close()`.

```python
soubor.close()
```

### Příkaz `with`

Pro zjednodušení práce se soubory a automatické uzavření souboru můžeme použít příkaz `with`.

```python
with open("muj_soubor.txt", "r") as soubor:
  obsah = soubor.read()
  print(obsah)
# Soubor se automaticky zavře po ukončení bloku with
```