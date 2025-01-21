**Zadání úkolu: Analýza faktorů ovlivňujících studijní výsledky**

**Cíl:** Cílem tohoto úkolu je prozkoumat a analyzovat dataset o faktorech ovlivňujících studijní výsledky studentů s využitím knihoven `pandas`, `matplotlib` a `scipy`. Z dat budete extrahovat užitečné informace, vizualizovat je a pokusíte se zodpovědět na několik výzkumných otázek.

**Datový soubor:** Dataset je dostupný zde: [https://www.kaggle.com/datasets/stealthtechnologies/predict-student-performance-dataset](https://www.kaggle.com/datasets/stealthtechnologies/predict-student-performance-dataset). Stáhněte si soubor `data.csv` a uložte ho do svého pracovního adresáře.

**Dataset obsahuje následující sloupce:**

*   `Study Hours`: Průměrný počet hodin studia denně.
*   `Sleep Hours`: Průměrný počet hodin spánku denně.
*   `Socioeconomic Score`: Normalizované skóre (0-1) vyjadřující socioekonomické zázemí studenta.
*   `Attendance (%)`: Procento zúčastněných hodin výuky.
*   `Grades`: Celkové hodnocení studenta (finální známka).

**Úkoly:**

1.  **Načtení a příprava dat (pandas):**

    *   Načtěte data ze souboru `data.csv` do `pandas` DataFrame.
    *   Prozkoumejte strukturu datasetu (počet řádků, sloupců, typy dat).
    *   Ověřte, zda data neobsahují chybějící hodnoty (NaN). Pokud ano, rozhodněte, jak s nimi naložíte (např. odstranění, nahrazení průměrem). Zdůvodněte svoje rozhodnutí.

2.  **Základní statistiky a průzkum dat (pandas, scipy):**

    *   Pomocí `pandas` vypočítejte průměrné, minimální a maximální hodnoty pro každý sloupec.
    *   Vypočítejte korelaci mezi všemi sloupci pomocí `pandas.DataFrame.corr` nebo `scipy.stats.pearsonr`. Interpretujte výsledky. Zaměřte se především na korelaci s cílovou proměnnou `Grades`.
    *   Pomocí `pandas` zjistěte, kolik studentů má `Grades` nad a kolik pod průměrem.

3.  **Vizualizace dat (matplotlib):**

    *   Vytvořte histogramy pro sloupce `Study Hours`, `Sleep Hours`, `Socioeconomic Score`, `Attendance (%)` a `Grades`.
    *   Vytvořte bodový graf (scatter plot) zobrazující vztah mezi `Study Hours` a `Grades`.
    *   Vytvořte bodový graf (scatter plot) zobrazující vztah mezi `Attendance (%)` a `Grades`.
    *   Přidejte do obou bodových grafů regresní přímku pomocí `matplotlib` a/nebo `scipy`.
    *   Vytvořte krabicový graf (box plot) zobrazující rozdělení `Grades` pro různé rozsahy `Study Hours` (např. 0-2 hodiny, 2-4 hodiny, 4-6 hodin, atd.).
    *   Všechny grafy správně pojmenujte (název grafu, popisky os, legenda).

4.  **Pokročilá analýza (pandas, scipy, volitelné):**

    *   Pomocí T-testu z knihovny `scipy.stats` zjistěte, zda existuje statisticky významný rozdíl v průměrných `Grades` mezi studenty s nadprůměrnou a podprůměrnou docházkou (`Attendance (%)`).
    *   Rozdělte studenty do skupin podle `Socioeconomic Score` (např. nízké, střední, vysoké) a porovnejte jejich průměrné `Grades`.

**Výzkumné otázky:**

Vaše analýza by se měla pokusit zodpovědět (mimo jiné) na následující otázky:

*   Jaký vliv má doba studia na studijní výsledky (`Grades`)?
*   Jaký vliv má docházka na studijní výsledky (`Grades`)?
*   Existuje korelace mezi socioekonomickým zázemím a studijními výsledky?
*   Jaký je vztah mezi délkou spánku a studijními výsledky?

**Pokyny pro začátečníky:**

*   **Pandas:** Zaměřte se na funkce jako `read_csv()`, `head()`, `describe()`, `mean()`, `min()`, `max()`, `corr()`, `fillna()`, `dropna()`, a práci se sloupci.
*   **Matplotlib:** Začněte s jednoduchými grafy (`hist()`, `scatter()`, `boxplot()`) a postupně přidávejte další prvky jako popisky, legendy, barvy a regresní přímku.
*   **Scipy:** Pro tento úkol se zaměřte na modul `scipy.stats` a jeho funkce pro výpočet korelace (`pearsonr`) a T-test (`ttest_ind`).
*   Nebojte se vyhledávat informace v dokumentaci a na internetu a používat LLM.