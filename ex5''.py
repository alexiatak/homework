#speed of vector calculations
import numpy as np
import scipy
from time import time
import math
import random
from matplotlib import pyplot as plt
import statistics

class MyList(list):
	def __init__(self, lst):
		super().__init__(lst)

	def __mul__(self, other):
		return MyList([self[_] * other[_] for _ in range(len(self))])

def average(lst):
	return sum(lst)/len(lst)

def stand_deviation(lst):
	sd=statistics.stdev(lst)
	return sd

j=10

def one_dim_list(j)
	Alist=MyList([MyList([randint(10,100)]*j)])
	Blist=MyList([MyList([randint(10,100)]*j)])
	return one_dim

def two_dim_list(j)
	Alist=MyList([MyList([randint(10,100)]*j) for col in range(j)])
	Blist=MyList([MyList([randint(10,100)]*j) for col in range(j)])
	return two_dim

def three_dim_list(j)
	Alist=MyList([MyList([MyList([randint(10,100)]*j)for col in range(j)]) for row in range(j)])
	Blist=MyList([MyList([MyList([randint(10,100)]*j)for col in range(j)]) for row in range(j)])
	return three_dim

colours = ["#FF7F50", "#00FFFF", "#FFD700"]
sample_size=20
averaget=[]
runtime=[]
sigma=[]
sizee=10

#test for one dim list
one_dim_list(j)
for i in range(sample_size):
		starting=time()
		Alist*Blist
		finishing=time()
		runtime.append(finishing-starting)
		averaget.append(average(runtime))
		sigma.append(stand_deviation(runtime))
#drawing for 1 dim list
plt.errorbar(n ,averaget, yerr=sigma, fmt="o", ecolor=colours[0], capsize=3, color=colours[0], label=f"{1}-dimension list")
plt.legend(fontsize=12)
plt.plot(sizee, averaget, color=colours[0])

#same for 2 dim list
two_dim_list(j)
for i in range(sample_size):
		starting=time()
		Alist*Blist
		finishing=time()
		runtime.append(finishing-starting)
		averaget.append(average(runtime))
		sigma.append(stand_deviation(runtime))
#drawing for 2 dim list
plt.errorbar(n ,averaget, yerr=sigma, fmt="o", ecolor=colours[1], capsize=3, color=colours[1], label=f"{2}-dimension list")
plt.legend(fontsize=12)
plt.plot(sizee, averaget, color=colours[1])

#same for 3 dim list
three_dim_list(j)
for i in range(sample_size):
		starting=time()
		Alist*Blist
		finishing=time()
		runtime.append(finishing-starting)
		averaget.append(average(runtime))
		sigma.append(stand_deviation(runtime))
#drawing for 3 dim list
plt.errorbar(n ,averaget, yerr=sigma, fmt="o", ecolor=colours[2], capsize=3, color=colours[2], label=f"{3}-dimension list")
plt.legend(fontsize=12)
plt.plot(sizee, averaget, color=colours[2])
