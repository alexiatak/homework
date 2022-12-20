from multiprocessing import Process as pr
import time

def examplee(x):
	sqr=x*x
	return sqr


if __name__=='__main__':
	runtime=[]
	all_pr=[]
	x=1000000000

	while True:
		for i in range(48):
			example_pr=pr(target=examplee, args=(x, ))
			all_pr.append(example_pr)
			for example_pr in all_pr:
				example_pr.start()
			starting=time.time()
			for example_pr in all_pr:
				example_pr.join()
			finishing=time.time()
			runtime.append(finishing-starting)
			if runtime[i]>runtime[i-1]:
				break
	print(f"Cores in this pc:{i}")
