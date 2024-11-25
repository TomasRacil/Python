class Pes:
  """Třída reprezentující psa."""
  def __init__(self, jmeno, rasa):
    """Konstruktor třídy."""
    self.jmeno = jmeno
    self.rasa = rasa

  def zastekej(self):
    """Metoda pro štěkání."""
    print("Haf!")

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

from abc import ABC, abstractmethod

class Zvire(ABC):
  @abstractmethod
  def vydavat_zvuk(self):
    pass

class Pes(Zvire):
  def vydavat_zvuk(self):
    print("Haf!")

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

# Vytvoření objektů
muj_pes = Pes("Rex", "labrador")
muj_pes.zastekej()

clovek = Clovek(30)
print(clovek.vek)
clovek.vek = 40
print(clovek.vek)