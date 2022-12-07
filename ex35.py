#changes in directory
import os
import datetime
import time
  
myadress=os.getcwd()

def scanner(adress):
	while(True):
		dir_list = os.listdir(adress)
		dir_before=set(dir_list)
		time.sleep(1)
		dir_list = os.listdir(adress)	
		dir_after=set(dir_list)
		timee=datetime.datetime.now()
		
		if dir_before != dir_after :
			if dir_before.difference(dir_after) != set():
				print (f"in { timee } , {dir_before.difference(dir_after)} was removed")
			if dir_after.difference(dir_before) != set():
				print (f"in { timee } , {dir_after.difference(dir_before)} was created")

scanner(myadress)
