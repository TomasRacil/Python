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