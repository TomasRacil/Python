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