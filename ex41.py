from multiprocessing import Process as pr
import time
import math

def examplee(x):
	res = 0
	for _ in range(math.ceil(x)):
		res += 1
	return res


if __name__=='__main__':
	runtime=[]
	all_pr=[]
	x=10000000

	for i in range(1, 48):
		all_pr = []
		print(f"i = {i}")
		for j in range(1, i + 1):
			all_pr.append(pr(target=examplee, args=(x / i, )))
		print(all_pr)
		for example_pr in all_pr:
			example_pr.start()
		starting=time.time()
		print(starting)
		for example_pr in all_pr:
			example_pr.join()
		finishing=time.time()
		print(finishing)
		runtime.append(finishing-starting)
		print(runtime[-1])
		if i > 1 and runtime[i-1]>runtime[i-2]:
			break
	print(f"Cores in this pc:{i}")
