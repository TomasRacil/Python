import threading
from time import time
import queue

def is_prime(num:int):
    if num<2: return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0: return False
    return True

queueLock = threading.Lock()
workQueue = queue.Queue(1000000)

class myThread (threading.Thread):
   def __init__(self, threadID, name, q, start, stop, step):
      super().__init__()
      self.threadID = threadID
      self.name = name
      self.q = q
      self.first = start
      self.stop = stop
      self.step = step
   def run(self):
      for i in range(self.first,self.stop, self.step):
          if is_prime(i):
              queueLock.acquire()
              workQueue.put(i)
              queueLock.release()

threadList = ["Thread-1", "Thread-2", "Thread-3","Thread-4"]
threads = []
threadID = 1

# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName, workQueue,threadID,threadID, len(threadList))
   threads.append(thread)
   threadID += 1

def solve_primes_threads(max_number:int):
    for thread in threads:
        thread.stop = max_number
        thread.start()

primes=[] 

def solve_primes_basic(max_number:int):
    for i in range(max_number):
        if is_prime(i): primes.append(i)  
    
if __name__ == "__main__":
    start = time()
    solve_primes_threads(1000000)
    print(f"Execution of threads: {time()-start}")
    for t in threads:
        t.join()
    print(workQueue.qsize())
    del workQueue
    
    start = time()
    solve_primes_basic(1000000)
    print(f"Execution of threads: {time()-start}")
    print(len(primes))