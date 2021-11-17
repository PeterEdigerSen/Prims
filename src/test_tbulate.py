from tabulate import tabulate

mydata = []
n = 100000000
n_prime = 5761455
n_prime_sen = 5761460
runtime = 4219.86
runtime_sen = 3342.28
mydata.append([n, n_prime, n_prime_sen, runtime, runtime_sen])
head = ["n", "n of prims", "n of prims SEN", "time in sec", "time in sec SEN"]
print(tabulate(mydata, headers=head, tablefmt="fancy_grid"))
