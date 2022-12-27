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

def opti(f, x, y, n):
	args, _ = scipy.optimize.curve_fit(f, x, y)
	lb = min(x)
	rb = max(x)
	h = (rb - lb) / n
	return [[lb + j * h for j in range(n)], [f(lb + i * h, *(__ for __ in args)) for i in range(n)]]

def one_dim_list(j):
	Alist=MyList([random.randint(10,100)]*j)
	Blist=MyList([random.randint(10,100)]*j)
	return Alist, Blist

def two_dim_list(j):
	Alist=MyList([MyList([random.randint(10,100)]*j) for col in range(j)])
	Blist=MyList([MyList([random.randint(10,100)]*j) for col in range(j)])
	return Alist, Blist

def three_dim_list(j):
	Alist=MyList([MyList([MyList([random.randint(10,100)]*j) for col in range(j)]) for row in range(j)])
	Blist=MyList([MyList([MyList([random.randint(10,100)]*j) for col in range(j)]) for row in range(j)])
	return Alist, Blist

colours = ["#FF7F50", "#00FFFF", "#FFD700","#008000","#FF0000","#00008B"]
sample_size=7
averaget=[]
runtime=[]
sigma=[]

max_size = 1000000
n = []   #list size

plt.subplot(2, 1, 1)
plt.ylabel("t, s")
plt.title("List multiplication")

#test for one dim list
print("1-dimension:")
for j in range(1, max_size, math.floor(max_size / 10)):
	Alist, Blist = one_dim_list(j)
	runtime = []
	for i in range(sample_size):
		starting=time()
		Alist*Blist
		finishing=time()
		runtime.append(finishing-starting)
		print(f"{runtime[-1]} s")
	averaget.append(average(runtime))
	print(f"Average time: {averaget[-1]} s")
	sigma.append(stand_deviation(runtime))
	print(f"Sigma: {sigma[-1]} s")
	n.append(j)
#drawing for 1 dim list
plt.errorbar(n ,averaget, yerr=sigma, fmt="o", ecolor=colours[0], capsize=3, color=colours[0], label=f"{1}-dimension list")
plt.legend(fontsize=12)
Line = opti((lambda x, a, b: a * x + b), n, averaget, 1000)
plt.plot(Line[0],Line[1],color=colours[0])


#same for 2 dim list
averaget=[]
sigma=[]
n = []
print("2-dimension:")
for j in range(1, math.ceil(math.sqrt(max_size)), math.floor(math.sqrt(max_size) / 10)):
	Alist, Blist = two_dim_list(j)
	runtime = []
	for i in range(sample_size):
		starting=time()
		Alist*Blist
		finishing=time()
		runtime.append(finishing-starting)
		print(f"{runtime[-1]} s")
	averaget.append(average(runtime))
	print(f"Average time: {averaget[-1]} s")
	sigma.append(stand_deviation(runtime))
	print(f"Sigma: {sigma[-1]} s")
	n.append(j ** 2)
#drawing for 2 dim list
plt.errorbar(n ,averaget, yerr=sigma, fmt="o", ecolor=colours[1], capsize=3, color=colours[1], label=f"{2}-dimension list")
plt.legend(fontsize=12)
Line = opti((lambda x, a, b: a * x + b), n, averaget, 1000)
plt.plot(Line[0],Line[1],color=colours[1])

#same for 3 dim list
averaget=[]
sigma=[]
n = []
print("3-dimension:")
for j in range(1, math.ceil(max_size ** (1 / 3)), math.floor(max_size ** (1 / 3) / 10)):
	Alist, Blist = three_dim_list(j)
	runtime = []
	for i in range(sample_size):
		starting=time()
		Alist*Blist
		finishing=time()
		runtime.append(finishing-starting)
		print(f"{runtime[-1]} s")
	averaget.append(average(runtime))
	print(f"Average time: {averaget[-1]} s")
	sigma.append(stand_deviation(runtime))
	print(f"Sigma: {sigma[-1]} s")
	n.append(j ** 3)
#drawing for 3 dim list
plt.errorbar(n ,averaget, yerr=sigma, fmt="o", ecolor=colours[2], capsize=3, color=colours[2], label=f"{3}-dimension list")
plt.legend(fontsize=12)
Line = opti((lambda x, a, b: a * x + b), n, averaget, 1000)
plt.plot(Line[0],Line[1],color=colours[2])

#creating np one dim array
def one_dim_array(j):
	Aarray=np.random.randint(low=10, high=100, size=(j))
	Barray=np.random.randint(low=10, high=100, size=(j))
	return Aarray , Barray

def two_dim_array(j):
	Aarray=np.random.randint(low=10, high=100, size=(j, j))
	Barray=np.random.randint(low=10, high=100, size=(j, j))
	return Aarray , Barray

def three_dim_array(j):
	Aarray=np.random.randint(low=10, high=100, size=(j, j, j))
	Barray=np.random.randint(low=10, high=100, size=(j, j, j))
	return Aarray , Barray



sample_size=20
aaveraget=[]
aruntime=[]
asigma=[]

max_size = 1000000
an = []   #array size

plt.subplot(2, 1, 2)
plt.xlabel("list length")
plt.ylabel("t, s")
plt.title("Array multiplication")

#test for one dim array
print("1-dimension:")
for j in range(1, max_size, math.floor(max_size / 10)):
	Aarray, Barray = one_dim_array(j)
	print(Aarray)
	runtime = []
	for i in range(sample_size):
		starting=time()
		Aarray*Barray
		finishing=time()
		aruntime.append(finishing-starting)
		print(f"{aruntime[-1]} s")
	aaveraget.append(average(aruntime))
	print(f"Average time: {aaveraget[-1]} s")
	asigma.append(stand_deviation(aruntime))
	print(f"Sigma: {asigma[-1]} s")
	an.append(j)
#drawing for 1 dim array
plt.errorbar(an ,aaveraget, yerr=asigma, fmt="o", ecolor=colours[3], capsize=3, color=colours[3], label=f"{1}-dimension list")
plt.legend(fontsize=12)
Line = opti((lambda x, a, b: a * x + b), an, aaveraget, 1000)
plt.plot(Line[0],Line[1],color=colours[3])

#same for 2 dim array
aaveraget=[]
asigma=[]
an = []
print("2-dimension:")
for j in range(1, math.ceil(math.sqrt(max_size)), math.floor(math.sqrt(max_size) / 10)):
	Aarray, Barray = two_dim_array(j)
	print(Aarray)
	aruntime = []
	for i in range(sample_size):
		starting=time()
		Aarray*Barray
		finishing=time()
		aruntime.append(finishing-starting)
		print(f"{aruntime[-1]} s")
	aaveraget.append(average(aruntime))
	print(f"Average time: {aaveraget[-1]} s")
	asigma.append(stand_deviation(aruntime))
	print(f"Sigma: {asigma[-1]} s")
	an.append(j ** 2)
#drawing for 2 dim array
plt.errorbar(an ,aaveraget, yerr=asigma, fmt="o", ecolor=colours[4], capsize=3, color=colours[4], label=f"{2}-dimension list")
plt.legend(fontsize=12)
Line = opti((lambda x, a, b: a * x + b), an, aaveraget, 1000)
plt.plot(Line[0],Line[1],color=colours[4])


#same for 3 dim array
aaveraget=[]
asigma=[]
an = []
print("3-dimension:")
for j in range(1, math.ceil(max_size ** (1 / 3)), math.floor(max_size ** (1 / 3) / 10)):
	Aarray, Barray = three_dim_array(j)
	print(Aarray)
	aruntime = []
	for i in range(sample_size):
		starting=time()
		Aarray*Barray
		finishing=time()
		aruntime.append(finishing-starting)
		print(f"{aruntime[-1]} s")
	aaveraget.append(average(aruntime))
	print(f"Average time: {aaveraget[-1]} s")
	asigma.append(stand_deviation(aruntime))
	print(f"Sigma: {asigma[-1]} s")
	an.append(j ** 3)
#drawing for 3 dim array
plt.errorbar(an ,aaveraget, yerr=asigma, fmt="o", ecolor=colours[5], capsize=3, color=colours[5], label=f"{3}-dimension list")
plt.legend(fontsize=12)
Line = opti((lambda x, a, b: a * x + b), an, aaveraget, 1000)
plt.plot(Line[0],Line[1],color=colours[5])

plt.show()
