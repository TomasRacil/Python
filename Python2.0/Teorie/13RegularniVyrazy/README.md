## Regulární výrazy

### Úvod

Regulární výrazy jsou mocným nástrojem pro práci s textem. Umožňují nám definovat vzory a hledat v textu řetězce, které těmto vzorům odpovídají. V Pythonu se pro práci s regulárními výrazy používá modul `re`.

### Modul `re`

Modul `re` obsahuje funkce pro práci s regulárními výrazy. Nejdůležitější z nich jsou:

* **`search(vzor, text)`:**  Hledá první výskyt vzoru v textu.
* **`findall(vzor, text)`:**  Hledá všechny výskyty vzoru v textu a vrací je jako seznam.
* **`split(vzor, text)`:**  Rozdělí text podle vzoru a vrátí seznam částí.
* **`sub(vzor, nahrada, text)`:**  Nahradí všechny výskyty vzoru v textu nahradou.

### Syntaxe regulárních výrazů

Regulární výrazy se skládají ze speciálních znaků a sekvencí, které definují vzor. Zde jsou některé základní:

* **`.`:**  Odpovídá libovolnému znaku (kromě nového řádku).
* **`*`:**  Odpovídá nula nebo více opakováním předchozího znaku.
* **`+`:**  Odpovídá jednomu nebo více opakováním předchozího znaku.
* **`?`:**  Odpovídá nula nebo jednomu opakování předchozího znaku.
* **`{m}`:**  Odpovídá přesně `m` opakováním předchozího znaku.
* **`{m,n}`:** Odpovídá `m` až `n` opakováním předchozího znaku.
* **`[]`:**  Definuje množinu znaků (např. `[a-z]` odpovídá libovolnému malému písmenu).
* **`|`:**  Odpovídá buď výrazu vlevo, nebo vpravo (OR).
* **`^`:**  Odpovídá začátku řetězce.
* **`$`:**  Odpovídá konci řetězce.
* **`\d`:**  Odpovídá libovolné číslici (0-9).
* **`\D`:**  Odpovídá libovolnému znaku, který není číslicí.
* **`\s`:**  Odpovídá libovolnému bílému znaku (mezera, tabulátor, nový řádek).
* **`\S`:**  Odpovídá libovolnému znaku, který není bílý znak.
* **`\w`:**  Odpovídá libovolnému alfanumerickému znaku (a-z, A-Z, 0-9, _).
* **`\W`:**  Odpovídá libovolnému znaku, který není alfanumerický.
* **`\b`:**  Odpovídá hranici slova.
* **`\B`:**  Odpovídá znaku, který není na hranici slova.

Pro testování různých regulárních výrazů je možné využít [tuto stránku](https://regex101.com/).

### Příklad

```python
import re

text = "Email pana Kolika je kolik@email.com.\nTento email nemá pan Kolík již 5 let."

# Nalezení emailové adresy
email_vzor = r"([a-z\d]+[a-z\d\.-_]*[a-z0-9]+)@(\w+.\w{2,3})"
emaily = re.findall(email_vzor, text)
print(f"Nalezené emaily: {emaily}")  # Vypíše: [('kolik', 'email.com')]

# Nahrazení textu
novy_text = re.sub(r"[kK]ol[ií]k", "Ladan", text)
print(f"Záměna kolik za Ladan: {novy_text}")
```
