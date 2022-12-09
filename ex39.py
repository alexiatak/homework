#data storage
import shelve
import random

def my_random_list():
	newlist=random.sample(range(0, 1000),100)
	
	with shelve.open("randomlist", flag="c") as s:
		s["list"] = newlist
	
def random_summ():
	with shelve.open("randomlist", flag="c") as s:
		liist=list(s["list"])
		rsum=sum(liist)
	return(rsum)

if __name__ == "__main__":
	my_random_list()
	print(random_summ())
