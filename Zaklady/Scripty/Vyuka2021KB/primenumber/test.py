import threading
from queue import Queue
from time import time



def is_prime(num:int)->bool:
    if num<2: return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0: return False
    return True

def solve_primes(max_number:int):
    primes = []
    for i in range(max_number):
        if is_prime(i): primes.append(i)
    return(len(primes))
        
##### Vicevlaknova sekce

class myThread (threading.Thread):
    def __init__(self, threadID:int, beg:int, end:int, step:int):
       super().__init__()
       self.threadID = threadID
       self.beg =beg
       self.end = end
       self.step = step
       self.p = []
    def run(self):
        for i in range(self.beg,self.end,self.step):
            if is_prime(i): self.p.append(i)
    def join(self):
        threading.Thread.join(self)
        return self.p

def solve_primes_2(max_number:int, thread_number)->list:
    threads = []
    primes = []
    thread_id = 1
    for thread_id in range(thread_number):
        thread = myThread(thread_id,thread_id,max_number,thread_number)
        thread.start()
        threads.append(thread)
        thread_id+=1
    for t in threads:
        primes.extend(t.join())
    
    return(len(primes))
if __name__ == "__main__":
    start = time()
    print(solve_primes(1000000))
    print(f"Elapsed time normal execution: {time()-start}")
    
    
    start = time()
    print(solve_primes_2(1000000,5))
    print(f"Elapsed time normal execution: {time()-start}")