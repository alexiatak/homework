#interaction of threads

import threading
import queue
import random
import time


class Receiver(threading.Thread):
	def __init__(self, q):
		self.queue = q
		self.sent = []

		def calc(qq):
			for threead in self.sent:
				while threead.is_alive():
					if not qq.empty():   
						numbr = qq.get_nowait()
						print(f"f({numbr}) = {(numbr**2)}")

		super().__init__(target=calc, args=(self.queue))

	def sent_list(self, send):
		self.sent.append(send)
			

class Sender(threading.Thread):
		def __init__(self, q, datanum, rec):
			self.queue=q
			self.receiver = rec
			
			def randomlist(qq):
				for i in range(datanum):
					time.sleep(random.randint(0, 4))
					values=random.randint(0,100)
					qq.put(values,block=False)
					print(f"VALUE :{values}")
					
			super().__init__(target=randomlist, args=(self.queue, ))
			self.receiver.sent_list(self)			

q = queue.Queue(15)
exampl = Receiver(q)
for i in range(3):
    s = Sender(q, 5, exampl)
    s.start()
exampl.start()
