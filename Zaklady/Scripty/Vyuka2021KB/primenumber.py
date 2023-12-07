# import threading
import timeit

def is_prime(num:int):
    if num<2: return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0: return False
    return True

primes=[]
def solve_primes(max_number:int):
    for i in range(max_number):
        if is_prime(i): primes.append(i)

print(len(primes))
print(timeit.timeit(lambda: solve_primes(100000), number=100))