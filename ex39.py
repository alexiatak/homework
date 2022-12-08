#data storage
import shelve
import random

newlist=random.sample(range(0, 1000),100)
print(newlist)
open('randomlist', flag = 'c', protocol=None, writeback = False)

s = shelve.open("randomlist")
for i in len(newlist):
	s[i]=newlist[i]
print(s.values)
s.close()
