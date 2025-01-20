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