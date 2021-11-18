from tabulate import tabulate
from prime_numbers import *
from prime_numbers_sen import *
import time

mydata = []
start_time_global = time.time()
for k in range(1, 9):
    n = 10 ** k
    start_time = time.time()
    n_prime = n_of_prime_numbers(n)
    runtime = time.time() - start_time
    start_time = time.time()
    n_prime_sen = n_of_prime_numbers_sen(n)
    runtime_sen = time.time() - start_time
    mydata.append([n, n_prime, n_prime_sen, runtime, runtime_sen])
runtime_global = time.time() - start_time_global
mydata.append(["Total time", "", "", runtime_global])

head = ["n", "n of prims", "n of prims SEN", "time in sec", "time in sec SEN"]
print(tabulate(mydata, headers=head, tablefmt="fancy_grid"))
