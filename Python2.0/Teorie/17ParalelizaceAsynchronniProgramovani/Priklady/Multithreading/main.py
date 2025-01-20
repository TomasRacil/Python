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