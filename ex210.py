from functools import lru_cache
from math import sin

class FunctionCache:
	def __init__(self,fun):
		self.fun=fun
	
	@lru_cache
	def resuult(self,arg):
		r=self.fun(arg)
		return r

def square(arg):
    return arg**2
   
square_cached=FunctionCache(square)

print(square_cached.resuult(2))
print(square_cached.resuult(2))
