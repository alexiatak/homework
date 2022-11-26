class FunctionCaller:
	def __init__(self,fun):
		self.fun=fun
		self.liist = []
	
	def append_job(self,exercise): 
		self.liist.append(exercise)
		
	res=[]
	def call(self):
		if len(self.liist) != 0 :
			for i in range(len(self.liist)):
				res(i) == self.fun(self.liist(i))
				print (f"Calling for job {self.liist(i)} . RESULT" ,res(i))
			self.liist.clear()
		else:
			print("nothing to do")
			
from math import sin
caller=FunctionCaller(sin)
caller.append_job(0)
caller.append_job(1)
caller.append_job(3.1415)
caller.call()
caller.call()
