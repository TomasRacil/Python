# Paralelizace a Asynchronní Programování v Pythonu

## Obsah

1.  [Úvod do Paralelizace](#uvod-do-paralelizace)
    *   [Sériové vs. Paralelní Zpracování](#seriove-vs-paralelni-zpracovani)
    *   [Výhody a Nevýhody Paralelizace](#vyhody-a-nevyhody-paralelizace)
2.  [Vícevláknové Programování (Threading)](#vicevlaknove-programovani-threading)
    *   [Co je Vlákno?](#co-je-vlakno)
    *   [Modul `threading`](#modul-threading)
    *   [Globální Zámek Interpreta (GIL)](#globalni-zamek-interpreta-gil)
    *   [Příklad Vícevláknové Aplikace](#priklad-vicevlaknove-aplikace)
3.  [Víceprocesové Programování (Multiprocessing)](#viceprocesove-programovani-multiprocessing)
    *   [Co je Proces?](#co-je-proces)
    *   [Modul `multiprocessing`](#modul-multiprocessing)
    *   [Obejití GILu](#obejiti-gilu)
    *   [Příklad Víceprocesové Aplikace](#priklad-viceprocesove-aplikace)
4.  [Sdílení Paměti a Synchronizace](#sdileni-pameti-a-synchronizace)
    *   [Problémy Souběžného Přístupu](#problemy-soubezneho-pristupu)
    *   [Sdílení Paměti v Threadingu](#sdileni-pameti-v-threadingu)
    *   [Sdílení Paměti v Multiprocessingu](#sdileni-pameti-v-multiprocessingu)
    *   [Synchronizační Primitiva](#synchronizacni-primitiva)
        *   [Zámky (Locks)](#zamky-locks)
        *   [Semafory (Semaphores)](#semafory-semaphores)
        *   [Bariéry (Barriers)](#bariery-barriers)
        *   [Podmínkové Proměnné (Condition Variables)](#podminkove-promenne-condition-variables)
5.  [Asynchronní Programování](#asynchronni-programovani)
    *   [Co je Asynchronní Programování?](#co-je-asynchronni-programovani)
    *   [Klíčová Slova `async` a `await`](#klicova-slova-async-a-await)
    *   [Knihovna `asyncio`](#knihovna-asyncio)
    *   [Událostmi Řízená Smyčka (Event Loop)](#udalostmi-rizena-smycka-event-loop)
    *   [Korutiny (Coroutines)](#korutiny-coroutines)
    *   [Úlohy (Tasks)](#ulohy-tasks)
    *   [Příklad Asynchronní Aplikace](#priklad-asynchronni-aplikace)
    *   [Kdy Použít Asynchronní Programování?](#kdy-pouzit-asynchronni-programovani)
6.  [Závěr](#zaver)
7.  [Další Zdroje](#dalsi-zdroje)

## <a id="uvod-do-paralelizace"></a> 1\. Úvod do Paralelizace

### <a id="seriove-vs-paralelni-zpracovani"></a> Sériové vs. Paralelní Zpracování

  * **Sériové (sekvenční) zpracování:** Úlohy jsou prováděny jedna po druhé. Dokud se nedokončí jedna úloha, nezačne se provádět další.
  * **Paralelní zpracování:** Více úloh se provádí současně, čímž se zkracuje celková doba zpracování.

### <a id="vyhody-a-nevyhody-paralelizace"></a> Výhody a Nevýhody Paralelizace

**Výhody:**

  * **Zvýšení výkonu:** Paralelizace umožňuje rychlejší provádění úloh, zejména u výpočetně náročných operací nebo I/O operací (vstup/výstup, např. čtení z disku, síťová komunikace).
  * **Lepší využití hardwaru:** Moderní procesory mají více jader, která mohou být využita pro paralelní běh úloh.
  * **Zvýšení responsivity:** Programy nezamrzají při provádění dlouhotrvajících operací, protože tyto operace mohou běžet na pozadí v samostatném vlákně/procesu.

**Nevýhody:**

  * **Složitější programování:** Paralelní programování je obvykle složitější než sériové programování, protože je nutné řešit synchronizaci a sdílení dat mezi vlákny/procesy.
  * **Riziko chyb souběhu (race conditions):** Pokud více vláken/procesů přistupuje ke sdíleným datům bez řádné synchronizace, může dojít k nepředvídatelnému chování programu.
  * **Režie spojená s přepínáním kontextu:** Přepínání mezi vlákny/procesy má určitou režii, která může v některých případech snížit celkový výkon.
  * **Ladění:** Ladění paralerních programů může být náročnější.

## 2\. <a id="uvod-do-paralelizace"></a> Vícevláknové Programování (Threading)

### <a id="co-je-vlakno"></a> Co je Vlákno?

Vlákno (thread) je nejmenší jednotka zpracování, kterou může operační systém naplánovat na procesoru. V rámci jednoho procesu může běžet více vláken, která sdílejí stejný paměťový prostor.

### <a id="modul-threading"></a> Modul `threading`

Python poskytuje modul `threading` pro práci s vlákny. Umožňuje vytvářet nová vlákna, spouštět je, synchronizovat je a komunikovat mezi nimi.

**Základní třídy a funkce modulu `threading`:**

  * `Thread`: Třída reprezentující vlákno.
  * `start()`: Spustí vlákno.
  * `join()`: Počká na dokončení vlákna.
  * `Lock`: Zámek pro synchronizaci přístupu ke sdíleným prostředkům.
  * `RLock`: Reentrantní zámek (umožňuje vícenásobné uzamčení stejným vláknem).
  * `Semaphore`: Semafor pro omezení počtu vláken, která mohou současně přistupovat ke sdílenému prostředku.
  * `Condition`: Podmínková proměnná pro signalizaci mezi vlákny.
  * `Event`: Událost pro synchronizaci vláken.
  * `Barrier`: Bariéra pro synchronizaci vláken.

### <a id="globalni-zamek-interpreta-gil"></a> Globální Zámek Interpreta (GIL)

**GIL (Global Interpreter Lock)** je mutex, který v CPythonu (standardní implementace Pythonu) umožňuje v jeden moment běh pouze jednomu vláknu, i když je k dispozici více jader. GIL zjednodušuje implementaci CPythonu a správu paměti, ale **omezuje výkonnost vícevláknových aplikací u CPU-náročných úloh**.

**Důsledky GILu:**

  * Pro CPU-náročné úlohy (např. složité matematické výpočty) vícevláknové programování v CPythonu obvykle nepřináší zrychlení, protože vlákna nemohou běžet skutečně paralelně na více jádrech.
  * Vícevláknové programování je stále užitečné pro I/O-náročné úlohy (např. síťová komunikace, čtení/zápis na disk), protože vlákno může čekat na dokončení I/O operace, zatímco jiné vlákno pokračuje ve vykonávání.

### <a id="priklad-vicevlaknove-aplikace"></a> Příklad Vícevláknové Aplikace

```python
import threading
import time

def task(name, time_to_sleep):
  print(f"Vlákno {name}: start")
  time.sleep(time_to_sleep)  # Simulace I/O operace
  print(f"Vlákno {name}: konec")

# Vytvoření a spuštění dvou vláken
thread1 = threading.Thread(target=task, args=("1",2))
thread2 = threading.Thread(target=task, args=("2",1))

thread1.start()
thread2.start()

print("Hlavní vlákno: čekání na dokončení vláken...")
thread1.join()
thread2.join()

print("Hlavní vlákno: hotovo")
```

**Vysvětlení:**

  * Funkce `task` simuluje úlohu, která trvá 2 sekundy (např. čekání na odpověď ze serveru).
  * Vytvoří se dvě vlákna, která provádějí tuto úlohu.
  * `thread1.start()` a `thread2.start()` spustí vlákna.
  * `thread1.join()` a `thread2.join()` zajistí, že hlavní vlákno počká na dokončení obou vláken.

## <a id="viceprocesove-programovani-multiprocessing"></a> 3\. Víceprocesové Programování (Multiprocessing)

### <a id="co-je-proces"></a> Co je Proces?

Proces je instance běžícího programu. Každý proces má svůj vlastní paměťový prostor a je izolovaný od ostatních procesů.

### <a id="modul-multiprocessing"></a> Modul `multiprocessing`

Python poskytuje modul `multiprocessing` pro práci s procesy. Umožňuje vytvářet nové procesy, spouštět je, synchronizovat je a komunikovat mezi nimi.

**Základní třídy a funkce modulu `multiprocessing`:**

  * `Process`: Třída reprezentující proces.
  * `start()`: Spustí proces.
  * `join()`: Počká na dokončení procesu.
  * `Queue`: Fronta pro komunikaci mezi procesy.
  * `Pipe`: Roury pro komunikaci mezi procesy.
  * `Value`: Sdílená hodnota mezi procesy.
  * `Array`: Sdílené pole mezi procesy.
  * `Manager`: Správce pro vytváření sdílených objektů (slovníky, seznamy, atd.).
  * `Pool`: Bazén procesů pro paralelní provádění úloh.

### <a id="obejiti-gilu"></a> Obejití GILu

Každý proces má svůj vlastní interpret Pythonu a tedy i svůj vlastní GIL. To znamená, že **víceprocesové programování umožňuje obejít omezení GILu a skutečně paralelizovat CPU-náročné úlohy na více jádrech**.

### <a id="priklad-viceprocesove-aplikace"></a> Příklad Víceprocesové Aplikace

```python
import multiprocessing
import time

def task(name):
  print(f"Vlákno {name}: start")
  for i in range(100_000_000):  # Simulace CPU-náročné operace
    pass
  print(f"Vlákno {name}: konec")

if __name__ == '__main__':
  # Vytvoření a spuštění dvou procesů
  process1 = multiprocessing.Process(target=task, args=("1",))
  process2 = multiprocessing.Process(target=task, args=("2",))

  process1.start()
  process2.start()

  print("Hlavní proces: čekání na dokončení procesů...")
  process1.join()
  process2.join()

  print("Hlavní proces: hotovo")
```

**Vysvětlení:**

  * Funkce `task` simuluje CPU-náročnou úlohu, která trvá 2 sekundy.
  * Vytvoří se dva procesy, které provádějí tuto úlohu.
  * `process1.start()` a `process2.start()` spustí procesy.
  * `process1.join()` a `process2.join()` zajistí, že hlavní proces počká na dokončení obou procesů.
  * **Důležité:** Kód, který spouští procesy, musí být uvnitř bloku `if __name__ == '__main__':`. To je nezbytné pro správnou funkci na Windows.

## <a id="sdileni-pameti-a-synchronizace"></a> 4\. Sdílení Paměti a Synchronizace

### <a id="problemy-soubezneho-pristupu"></a> Problémy Souběžného Přístupu

Když více vláken/procesů přistupuje ke sdíleným datům (např. proměnným, souborům), může dojít k **chybám souběhu (race conditions)**. Tyto chyby nastávají, když výsledek operace závisí na nepředvídatelném pořadí, ve kterém vlákna/procesy přistupují ke sdíleným datům.

### <a id="sdileni-pameti-v-threadingu"></a> Sdílení Paměti v Threadingu

Vlákna v rámci jednoho procesu sdílejí stejný paměťový prostor. To znamená, že mohou přímo přistupovat ke stejným proměnným.

**Příklad chyby souběhu:**

```python
import threading
import time

counter = 0

def increment_counter():
    global counter
    for _ in range(10000):
        temp = counter
        temp += 1
        time.sleep(0)
        counter = temp

# Vytvoření a spuštění deseti vláken
threads = []
for i in range(10):
  t = threading.Thread(target=increment_counter)
  threads.append(t)
  t.start()

for t in threads:
  t.join()

print(f"Counter: {counter}")  # Očekávaná hodnota: 100000, ale bude pravděpodobně VÝRAZNĚ menší
```

**Vysvětlení:**

  * Dvě vlákna se snaží inkrementovat sdílenou proměnnou `counter`.
  * Operace `counter += 1` není atomická (skládá se z více kroků: přečtení hodnoty, inkrementace, zápis nové hodnoty).
  * Může se stát, že obě vlákna přečtou stejnou hodnotu `counter`, inkrementují ji a zapíší zpět. Tím se ztratí jedna inkrementace.

### <a id="sdileni-pameti-v-multiprocessingu"></a> Sdílení Paměti v Multiprocessingu

Procesy ve výchozím stavu nesdílejí paměť. Každý proces má svůj vlastní paměťový prostor. Pro sdílení dat mezi procesy je nutné použít speciální mechanismy:

  * **`Value` a `Array`:** Pro sdílení jednoduchých hodnot a polí.
  * **`Manager`:** Pro sdílení složitějších objektů (slovníky, seznamy).
  * **`Queue` a `Pipe`:** Pro předávání zpráv mezi procesy (data se kopírují).

**Příklad sdílení dat pomocí `Value`:**

```python
import multiprocessing

def increment_counter(shared_counter):
  for _ in range(100000):
    with shared_counter.get_lock(): # Získání zámku pro sdílenou proměnnou
      shared_counter.value += 1

if __name__ == '__main__':
  shared_counter = multiprocessing.Value('i', 0) # Sdílená proměnná typu integer (i) s počáteční hodnotou 0

  p1 = multiprocessing.Process(target=increment_counter, args=(shared_counter,))
  p2 = multiprocessing.Process(target=increment_counter, args=(shared_counter,))

  p1.start()
  p2.start()

  p1.join()
  p2.join()

  print(f"Counter: {shared_counter.value}") # Očekávaná hodnota: 200000
```

**Vysvětlení:**

  * `multiprocessing.Value('i', 0)` vytvoří sdílenou proměnnou typu integer s počáteční hodnotou 0.
  * `shared_counter.get_lock()` vrací zámek, který je nutné použít pro synchronizaci přístupu ke sdílené proměnné.
  * `with shared_counter.get_lock():` automaticky získá a uvolní zámek.

### <a id="synchronizacni-primitiva"></a> Synchronizační Primitiva

Synchronizační primitiva jsou nástroje, které umožňují koordinovat přístup ke sdíleným prostředkům a předcházet tak chybám souběhu.

#### <a id="zamky-locks"></a> Zámky (Locks)

Zámek (Lock) umožňuje exkluzivní přístup ke sdílenému prostředku. V jeden moment může zámek držet pouze jedno vlákno/proces.

  * **`threading.Lock`:** Základní zámek pro synchronizaci vláken.
  * **`multiprocessing.Lock`:** Základní zámek pro synchronizaci procesů.
  * **`acquire()`:** Získá zámek. Pokud je zámek již obsazený, vlákno/proces se zablokuje a čeká na jeho uvolnění.
  * **`release()`:** Uvolní zámek.

**Příklad použití zámku v threadingu:**

```python
import threading
import time

counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(10000):
        lock.acquire()
        try:
            temp = counter
            temp += 1
            time.sleep(0)
            counter = temp
        finally:
            lock.release()

# Vytvoření a spuštění deseti vláken
threads = []
for i in range(10):
  t = threading.Thread(target=increment_counter)
  threads.append(t)
  t.start()

for t in threads:
  t.join()

print(f"Counter: {counter}")  # Očekávaná hodnota: 100000, ale bude pravděpodobně VÝRAZNĚ menší
```

**Vysvětlení:**

  * `lock.acquire()` získá zámek. Pokud je zámek již uzamčen jiným vláknem, aktuální vlákno se zablokuje a čeká.
  * `lock.release()` uvolní zámek.
  * Blok `try...finally` zajišťuje, že zámek bude uvolněn i v případě výjimky.
  * Použití zámku zabraňuje chybě souběhu a zajišťuje správný výsledek.

#### <a id="semafory-semaphores"></a> Semafory (Semaphores)

Semafor je zobecněním zámku. Umožňuje nastavit, kolik vláken/procesů může současně přistupovat ke sdílenému prostředku.

  * **`threading.Semaphore(value=1)`:** Vytvoří semafor s počáteční hodnotou `value`.
  * **`multiprocessing.Semaphore(value=1)`:** Vytvoří semafor s počáteční hodnotou `value`.
  * **`acquire()`:** Sníží hodnotu semaforu o 1. Pokud je hodnota 0, vlákno/proces se zablokuje a čeká.
  * **`release()`:** Zvýší hodnotu semaforu o 1.

**Příklad použití semaforu:**

```python
import threading
import time

semaphore = threading.Semaphore(2) # Povoluje přístup maximálně 2 vláknům

def access_resource(thread_id):
  print(f"Vlákno {thread_id} se pokouší získat přístup...")
  semaphore.acquire()
  print(f"Vlákno {thread_id} získalo přístup.")
  time.sleep(2)  # Simulace práce se sdíleným prostředkem
  print(f"Vlákno {thread_id} uvolňuje přístup.")
  semaphore.release()

# Vytvoření a spuštění 4 vláken
threads = []
for i in range(4):
  t = threading.Thread(target=access_resource, args=(i+1,))
  threads.append(t)
  t.start()

for t in threads:
  t.join()
```

**Vysvětlení:**

  * Semafor je inicializován s hodnotou 2, takže maximálně 2 vlákna mohou současně přistupovat ke sdílenému prostředku.
  * Když se vlákno pokusí získat přístup pomocí `semaphore.acquire()`, hodnota semaforu se sníží o 1.
  * Pokud je hodnota semaforu 0, vlákno se zablokuje a čeká, dokud jiné vlákno neuvolní semafor pomocí `semaphore.release()`.

#### <a id="bariery-barriers"></a> Bariéry (Barriers)

Bariéra umožňuje synchronizovat skupinu vláken/procesů tak, že čeká, dokud všechna vlákna/procesy nedosáhnou určitého bodu v kódu.

  * **`threading.Barrier(parties)`:** Vytvoří bariéru pro `parties` počet vláken.
  * **`multiprocessing.Barrier(parties)`:** Vytvoří bariéru pro `parties` počet procesů.
  * **`wait()`:** Vlákno/proces zavolá `wait()` na bariéře. Vlákno/proces se zablokuje, dokud všechna vlákna/procesy nedosáhnou bariéry (nezavolají `wait()`).

**Příklad použití bariéry:**

```python
import threading
import time

barrier = threading.Barrier(3) # Bariéra pro 3 vlákna

def worker(thread_id):
  print(f"Vlákno {thread_id} dělá nějakou přípravnou práci...")
  time.sleep(thread_id) # Různá doba přípravné práce
  print(f"Vlákno {thread_id} čeká na bariéře...")
  barrier.wait()
  print(f"Vlákno {thread_id} pokračuje po bariéře.")

# Vytvoření a spuštění 3 vláken
threads = []
for i in range(3):
  t = threading.Thread(target=worker, args=(i+1,))
  threads.append(t)
  t.start()

for t in threads:
  t.join()
```

**Vysvětlení:**

  * Bariéra je vytvořena pro 3 vlákna.
  * Každé vlákno provádí nějakou přípravnou práci (simulovanou různou dobou spánku).
  * `barrier.wait()` způsobí, že se vlákno zablokuje, dokud všechna 3 vlákna nedosáhnou bariéry.
  * Po dosažení bariéry se všechna vlákna odblokují a pokračují v provádění.

#### <a id="podminkove-promenne-condition-variables"></a> Podmínkové Proměnné (Condition Variables)

Podmínková proměnná umožňuje vláknu/procesu čekat na splnění určité podmínky. Je vždy spojena se zámkem.

  * **`threading.Condition(lock=None)`:** Vytvoří podmínkovou proměnnou. Volitelně lze specifikovat zámek, jinak se vytvoří nový `RLock`.
  * **`multiprocessing.Condition(lock=None)`:** Vytvoří podmínkovou proměnnou. Volitelně lze specifikovat zámek, jinak se vytvoří nový `RLock`.
  * **`acquire()` a `release()`:** Metody pro získání a uvolnění přidruženého zámku.
  * **`wait()`:** Uvolní zámek a zablokuje vlákno/proces, dokud jiné vlákno/proces nezavolá `notify()` nebo `notify_all()` na stejné podmínkové proměnné. Po probuzení vlákno/proces znovu získá zámek.
  * **`notify()`:** Probudí jedno z vláken/procesů čekajících na podmínkové proměnné (pokud nějaké čeká).
  * **`notify_all()`:** Probudí všechna vlákna/procesy čekající na podmínkové proměnné.

**Příklad použití podmínkové proměnné:**

```python
import threading
import time

condition = threading.Condition()
data = []
ready = False

def consumer():
  global data, ready
  while True:
    with condition:
      while not ready:
        print("Consumer čeká na data...")
        condition.wait(2)
      print(f"Consumer obdržel data: {data.pop()}")
      ready = False
      condition.notify() # Notifikuje producer, že může přidat další data

def producer():
  global data, ready
  for i in range(5):
    with condition:
      while ready:
        print("Producer čeká na zpracování dat...")
        condition.wait()
      data.append(i)
      print(f"Producer přidal data: {i}")
      ready = True
      condition.notify() # Notifikuje consumer, že jsou data k dispozici
    time.sleep(1)

# Vytvoření a spuštění vláken
consumer_thread = threading.Thread(target=consumer)
producer_thread = threading.Thread(target=producer)

consumer_thread.start()
producer_thread.start()
```

**Vysvětlení:**

  * `condition` je podmínková proměnná sdílená mezi `consumer` a `producer`.
  * `consumer` čeká, dokud `ready` není `True`.
  * `producer` nastaví `ready` na `True` po přidání dat a notifikuje `consumer`.
  * `consumer` po obdržení notifikace zpracuje data, nastaví `ready` na `False` a notifikuje `producer`.
  * Použití `with condition:` automaticky zajišťuje získání a uvolnění zámku přidruženého k podmínkové proměnné.

## <a id="asynchronni-programovani"></a> 5\. Asynchronní Programování

### <a id="co-je-asynchronni-programovani"></a> Co je Asynchronní Programování?

Asynchronní programování je technika, která umožňuje provádět více úloh **zdánlivě** současně v **jediném vlákně** pomocí **událostmi řízené smyčky (event loop)**. Místo blokujícího čekání na dokončení I/O operace (např. síťový požadavek, čtení z disku) může program mezitím provádět jiné úlohy.

**Rozdíl oproti vícevláknovému programování:**

  * **Vícevláknové:** Využívá více vláken operačního systému, mezi kterými se přepíná.
  * **Asynchronní:** Využívá jedno vlákno a přepíná mezi úlohami v rámci tohoto vlákna, když nastane I/O událost.

### <a id="klicova-slova-async-a-await"></a> Klíčová Slova `async` a `await`

  * **`async def`:** Definuje asynchronní funkci, tzv. **korutinu (coroutine)**.
  * **`await`:** Používá se uvnitř asynchronní funkce k pozastavení provádění korutiny, dokud se nedokončí awaitovaná operace (např. I/O operace). Klíčové slovo `await` lze použít pouze uvnitř `async def` funkce.

### <a id="knihovna-asyncio"></a> Knihovna `asyncio`

`asyncio` je standardní knihovna Pythonu pro asynchronní programování. Poskytuje:

  * **Událostmi řízenou smyčku (event loop):** Základní mechanismus pro řízení asynchronních úloh.
  * **Korutiny (coroutines):** Funkce definované pomocí `async def`.
  * **Úlohy (tasks):** Objekty, které reprezentují asynchronní operace.
  * **Futures:** Objekty, které reprezentují výsledek asynchronní operace, který ještě není k dispozici.
  * Nástroje pro práci s asynchronními I/O operacemi, časovači, zámky, frontami atd.

### <a id="udalostmi-rizena-smycka-event-loop"></a> Událostmi Řízená Smyčka (Event Loop)

Event loop je srdcem asynchronního programu. Neustále monitoruje registrované I/O události a spouští příslušné korutiny, když jsou události aktivovány.

**Základní princip:**

1.  Registrace I/O událostí (např. "čekej na data ze socketu").
2.  Spuštění event loopu.
3.  Event loop čeká na události.
4.  Když nastane událost, event loop spustí příslušnou korutinu.
5.  Korutina běží, dokud nenarazí na `await`.
6.  `await` pozastaví korutinu a vrátí řízení event loopu.
7.  Event loop pokračuje v monitorování událostí a spouštění jiných korutin.
8.  Když se awaitovaná operace dokončí, event loop znovu aktivuje pozastavenou korutinu.

### <a id="korutiny-coroutines"></a> Korutiny (Coroutines)

Korutiny jsou speciální funkce definované pomocí `async def`. Mohou být pozastaveny pomocí `await` a později znovu obnoveny.

```python
import asyncio

async def my_coroutine():
  print("Korutina spuštěna")
  await asyncio.sleep(1)  # Simulace I/O operace, pozastaví se na 1 sekundu
  print("Korutina pokračuje")

async def main():
  task = asyncio.create_task(my_coroutine()) #vytvoří task
  await task #zavolá task

asyncio.run(main()) # spustí hlavní async funkci
```

### <a id="ulohy-tasks"></a> Úlohy (Tasks)

Úlohy (Tasks) jsou objekty, které reprezentují asynchronní operace. Jsou vytvářeny z korutin pomocí `asyncio.create_task()`.

```python
import asyncio

async def my_coroutine():
  print("Korutina spuštěna")
  await asyncio.sleep(1)
  print("Korutina pokračuje")

async def main():
  # Vytvoření úlohy z korutiny
  task = asyncio.create_task(my_coroutine())

  print("Dělám něco jiného, zatímco úloha běží na pozadí...")

  # Čekání na dokončení úlohy
  await task

  print("Úloha dokončena")

asyncio.run(main())
```

### <a id="priklad-asynchronni-aplikace"></a> Příklad Asynchronní Aplikace

```python
import asyncio
import time

async def fetch_data(url):
  print(f"Začínám stahovat: {url}")
  await asyncio.sleep(2)  # Simulace síťového požadavku
  print(f"Dokončeno stahování: {url}")
  return f"Data z {url}"

async def main():
  start_time = time.time()

  # Vytvoření úloh pro stahování dat
  task1 = asyncio.create_task(fetch_data("url1"))
  task2 = asyncio.create_task(fetch_data("url2"))

  # Čekání na dokončení úloh
  data1 = await task1
  data2 = await task2

  end_time = time.time()
  print(f"Celkový čas: {end_time - start_time:.2f} sekund")
  print(f"Data 1: {data1}")
  print(f"Data 2: {data2}")

asyncio.run(main())
```

**Vysvětlení:**

  * `fetch_data` je asynchronní funkce, která simuluje stahování dat z URL.
  * `asyncio.create_task` vytvoří úlohy pro stahování dat ze dvou URL.
  * `await task1` a `await task2` čekají na dokončení úloh.
  * Program **zdánlivě** stahuje data z obou URL současně, i když běží v jediném vlákně.
  * Celkový čas stahování je přibližně 2 sekundy (doba trvání nejpomalejšího požadavku), nikoli 4 sekundy (součet dob trvání obou požadavků).

### <a id="kdy-pouzit-asynchronni-programovani"></a> Kdy Použít Asynchronní Programování?

Asynchronní programování je vhodné pro **I/O-bound úlohy**, kde program tráví hodně času čekáním na dokončení I/O operací (síťové požadavky, čtení/zápis na disk, interakce s uživatelem).

**Typické příklady:**

  * **Síťové aplikace:** Webové servery, chatovací aplikace, stahování souborů.
  * **GUI aplikace:** Udržování responsivity uživatelského rozhraní během provádění dlouhotrvajících operací.
  * **Práce s velkým množstvím souborů:** Asynchronní čtení/zápis z/do více souborů.

**Asynchronní programování není vhodné pro CPU-bound úlohy** (náročné výpočty), protože v CPythonu je stále omezeno na jedno vlákno a nepřináší zrychlení. Pro CPU-bound úlohy je vhodnější multiprocessing.

## <a id="zaver"></a> 6\. Závěr

Paralelizace a asynchronní programování jsou důležité koncepty pro efektivní využití moderního hardwaru a psaní responzivních aplikací. Python nabízí bohaté nástroje pro vícevláknové (threading), víceprocesové (multiprocessing) i asynchronní (asyncio) programování. Volba mezi těmito přístupy závisí na charakteru úlohy:

  * **I/O-bound úlohy:**
      * **Threading:** Vhodný pro jednoduché případy, kde není potřeba obcházet GIL.
      * **Asyncio:** Vhodný pro komplexnější aplikace s velkým množstvím I/O operací, poskytuje jemnější kontrolu nad prováděním úloh.
  * **CPU-bound úlohy:**
      * **Multiprocessing:** Vhodný pro paralelizaci výpočetně náročných úloh na více jádrech a obchází omezení GILu.

Správné použití synchronizačních primitiv je klíčové pro zajištění integrity dat a předcházení chybám souběhu ve vícevláknových a víceprocesových aplikacích.

## <a id="dalsi-zdroje"></a> 7\. Další Zdroje

  * [Dokumentace k modulu `threading`](https://docs.python.org/3/library/threading.html)
  * [Dokumentace k modulu `multiprocessing`](https://docs.python.org/3/library/multiprocessing.html)