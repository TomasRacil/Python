import threading
from queue import Queue
from time import time

from multiprocessing import Pool

def is_prime(num:int)->bool:
    if num<2: return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0: return False
    return True

def run(vals):
    primes=[]
    for i in range(*vals):
        if is_prime(i): 
            primes.append(i)
    return primes

if __name__ == '__main__':
    start = time()
    max = 1000000
    step = 5
    with Pool(5) as p:
        primes = [item for list in p.map(run, [(1,max,step), (2,max,step),(3,max,step), (4,max,step), (5,max,step)]) for item in list]
        print(len(primes))
    print(f"Elapsed time normal execution: {time()-start}")

