import time

def isPrime(n):
  for num in range(2, n//2):
    if n%num == 0:
      return False
  return True

def kth_prime(k):
  candidate = 2
  while k:
    if isPrime(candidate):
      k -= 1
    candidate += 1
  return candidate - 1

# Driver code
start_time = time.time()
print(kth_prime(1500)) 
print("--- %s seconds ---" % (time.time() - start_time))