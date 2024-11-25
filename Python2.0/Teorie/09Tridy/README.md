## Třídy

### Úvod do objektově orientovaného programování

Python je objektově orientovaný jazyk. To znamená, že se v něm pracuje s objekty, které mají své vlastnosti (atributy) a chování (metody). Třídy slouží jako šablony pro vytváření objektů. 

### Definice třídy

Třídu definujeme pomocí klíčového slova `class`, za kterým následuje název třídy a dvojtečka. Tělo třídy obsahuje odsazené definice atributů a metod.

```python
class Pes:
  """Třída reprezentující psa."""
  def __init__(self, jmeno, rasa):
    """Konstruktor třídy."""
    self.jmeno = jmeno
    self.rasa = rasa

  def zastekej(self):
    """Metoda pro štěkání."""
    print("Haf!")
```

V tomto příkladu definujeme třídu `Pes` s atributy `jmeno` a `rasa` a metodou `zastekej`.

### Konstruktor

Konstruktor je speciální metoda, která se volá při vytváření objektu. V Pythonu se konstruktor definuje jako metoda `__init__`.  Konstruktor slouží k inicializaci atributů objektu.

### Vytvoření objektu (instance)

Objekt (instanci) třídy vytvoříme zavoláním názvu třídy s argumenty pro konstruktor.

```python
muj_pes = Pes("Rex", "labrador")  # Vytvoření objektu třídy Pes
```

### Přístup k atributům a metodám

K atributům a metodám objektu přistupujeme pomocí tečkové notace.

```python
print(muj_pes.jmeno)  # Vypíše "Rex"
muj_pes.zastekej()  # Zavolá metodu zastekej()
```

### Modifikátory přístupu

V Pythonu neexistují striktní modifikátory přístupu jako `public`, `protected` a `private`. Místo toho se používají konvence:

* **Veřejné atributy a metody:**  jsou přístupné odkudkoliv.
* **Chráněné atributy a metody:**  začínají jedním podtržítkem (`_`).  Měly by být používány pouze v rámci třídy a jejích podtříd.
* **Privátní atributy a metody:**  začínají dvěma podtržítky (`__`).  Python je "mangluje", aby se ztížil přístup zvenčí.

### Dědičnost

Dědičnost umožňuje vytvářet nové třídy, které dědí vlastnosti a chování od existujících tříd.

```python
class Savec:
  """Rodičovská třída."""
  def __init__(self, jmeno):
    self.jmeno = jmeno

  def dychej(self):
    print("Dýchám.")

class Pes(Savec):
  """Podtřída dědící od třídy Savec."""
  def __init__(self, jmeno, rasa):
    super().__init__(jmeno)  # Volání konstruktoru rodičovské třídy
    self.rasa = rasa

  def zastekej(self):
    print("Haf!")
```

V tomto příkladu třída `Pes` dědí od třídy `Savec`.  Můžeme použít `super()` pro přístup k metodám rodičovské třídy.

### Abstraktní třídy

Abstraktní třídy slouží jako rozhraní a nemohou být instanciovány. Definují metody, které musí být implementovány v podtřídách.

```python
from abc import ABC, abstractmethod

class Zvire(ABC):
  @abstractmethod
  def vydavat_zvuk(self):
    pass

class Pes(Zvire):
  def vydavat_zvuk(self):
    print("Haf!")
```

V tomto příkladu `Zvire` je abstraktní třída s abstraktní metodou `vydavat_zvuk`. Třída `Pes` musí implementovat tuto metodu.

### Property dekorátor

Property dekorátor umožňuje definovat metody, které se chovají jako atributy. To je užitečné pro kontrolu přístupu k atributům.

```python
class Clovek:
  def __init__(self, vek):
    self._vek = vek

  @property
  def vek(self):
    return self._vek

  @vek.setter
  def vek(self, novy_vek):
    if novy_vek < 0:
      raise ValueError("Věk nemůže být záporný.")
    self._vek = novy_vek
```

V tomto příkladu `vek` se chová jako atribut, ale jeho hodnota je kontrolována setter metodou.
