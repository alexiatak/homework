class FunctionCaller:
	def __init__(self,fun):
		self.fun=fun
		self.liist = []
	@classmethod
	def append_job(cls,exercise):
		cls.liist.append(exercise)
		
	@classmethod
	def call(cls):
		for i in range(len(cls.liist)):
			print (f"Calling for job {exercise} . RESULT {cls(exercise)}")

from math import sin
caller=FunctionCaller(sin)
caller.append_job(0)
caller.call()
