import fastprime
import time

print(fastprime.__doc__)
start_time = time.time()
print(fastprime.add_one(1500)) 
print("--- %s seconds ---" % (time.time() - start_time))
