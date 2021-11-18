from tabulate import tabulate
from prime_numbers_sen import *
import time

mydata = []
mydata.append([1])
mydata.append([100])
mydata.append([100000])
mydata.append([999999])
mydata.append([1000000])
mydata.append([10000000])
mydata.append([100000000])
mydata.append([100000000])
mydata.append([1.1])
head = ["n of prims SEN"]
print(tabulate(mydata, headers=head, tablefmt="fancy_grid"))
