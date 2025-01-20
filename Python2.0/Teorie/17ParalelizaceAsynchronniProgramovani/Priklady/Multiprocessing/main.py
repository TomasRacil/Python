import threading
import multiprocessing
import time

def task(name):
  print(f"Vlákno {name}: start")
  for i in range(100_000_000):  # Simulace CPU-náročné operace
    pass
  print(f"Vlákno {name}: konec")

if __name__ == '__main__':
  start_time = time.time()

  # Vytvoření a spuštění dvou vláken
  thread1 = threading.Thread(target=task, args=("1",))
  thread2 = threading.Thread(target=task, args=("2",))

  thread1.start()
  thread2.start()

  print("Hlavní vlákno: čekání na dokončení vláken...")
  thread1.join()
  thread2.join()

  end_time = time.time()
  print(f"Hlavní vlákno: hotovo za {end_time - start_time:.4f} sekund")
  
  start_time = time.time()

  # Vytvoření a spuštění dvou procesů
  process1 = multiprocessing.Process(target=task, args=("1",))
  process2 = multiprocessing.Process(target=task, args=("2",))

  process1.start()
  process2.start()

  print("Hlavní proces: čekání na dokončení procesů...")
  process1.join()
  process2.join()

  end_time = time.time()
  print(f"Hlavní proces: hotovo za {end_time - start_time:.4f} sekund")