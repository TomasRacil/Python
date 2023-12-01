# import threading
import time

def is_prime(num:int):
    if num<2: return False
    for i in range(2,int(num**0.5)):
        if num%i == 0: return False
    return True

primes=[]

start = time.perf_counter()
for i in range(1000000):
    if is_prime(i): primes.append(i)
end = time.perf_counter()

print(end - start)