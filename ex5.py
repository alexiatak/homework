#speed of vector calculations
import numpy as np
import scipy
from time import time
import math
import random
from matplotlib import pyplot as plt
import statistics

def average(lst):
	return sum(lst)/len(lst)

def stand_deviation(lst):
	sd=statistics.stdev(lst)
	return sd

colours = ["#FF7F50", "#00FFFF", "#FFD700"]
sample_size=20
averaget=[]
runtime=[]
sigma=[]
sizee=10

for i in range(1,3):
	plt.subplot(1, 2, 1)
	plt.xlabel("Length of list")
	plt.ylabel("seconds")
	plt.title("List multiplication")
	
	Alist=list(np.random.randint(low = 0,high=200,size=sizee))
	Blist=list(np.random.randint(low = 0,high=200,size=sizee))

	for i in range(sample_size):
		starting=time()
		mult=[]
		for Al,Bl in zip(Alist,Blist):
			mult.append(Al*Bl)
		finishing=time()
		runtime.append(finishing-starting)
		averaget.append(average(runtime))
		sigma.append(stand_deviation(runtime))

		plt.errorbar(n ,averaget, yerr=sigma, fmt="o", ecolor=c[i], capsize=3, color=colours[i], label=f"{i}-dimension list")
		plt.legend(fontsize=12)
		plt.plot(sizee, averaget, color=c[i])
