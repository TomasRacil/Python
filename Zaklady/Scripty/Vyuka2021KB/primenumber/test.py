import threading
from queue import Queue
from time import time

primes = []

def is_prime(num:int)->bool:
    if num<2: return False
    for i in range(2,int(num**0.5)):
        if num%i == 0: return False
    return True

def solve_primes(max_number:int):
    for i in range(max_number):
        if is_prime(i): primes.append(i)
        
##### Vicevlaknova sekce

primes2 = Queue(100000)
queueLock = threading.Lock()

class myThread (threading.Thread):
   def __init__(self, threadID:int, beg:int, end:int, step:int):
      super().__init__()
      self.threadID = threadID
      self.beg =beg
      self.end = end
      self.step = step
   def run(self):
      for i in range(self.beg,self.end,self.step):
          if is_prime(i): 
              queueLock.acquire()
              primes2.put(i)
              queueLock.release()

def solve_primes_2(max_number:int, thread_number):
    threads = []
    threadID = 1
    for thread_id in range(thread_number):
        thread = myThread(thread_id,thread_id,max_number,thread_number)
        thread.start()
        threads.append(thread)
        thread_id+=1
    for t in threads:
        t.join()
if __name__ == "__main__":
    start = time()
    solve_primes(1000000)
    print(f"Elapsed time normal execution: {time()-start}")
    print(len(primes))
    
    start = time()
    solve_primes_2(1000000,4)
    print(f"Elapsed time normal execution: {time()-start}")
    print(primes2.qsize())