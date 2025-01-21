import threading
import time

semaphore = threading.Semaphore(2) # Povoluje přístup maximálně 2 vláknům

def access_resource(thread_id):
  while True:
    print(f"Vlákno {thread_id} se pokouší získat přístup...")
    if semaphore.acquire(timeout=1):
      print(f"Vlákno {thread_id} získalo přístup.")
      time.sleep(4)  # Simulace práce se sdíleným prostředkem
      print(f"Vlákno {thread_id} uvolňuje přístup.")
      semaphore.release()
      break

# Vytvoření a spuštění 4 vláken
threads = []
for i in range(4):
  t = threading.Thread(target=access_resource, args=(i+1,))
  threads.append(t)
  t.start()

for t in threads:
  t.join()