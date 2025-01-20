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