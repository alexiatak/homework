class Star(object):
	def __init__(self,absmag):
		self.absmag = absmag
		
sun = Star(absmag=1)
vega = Star(absmag=0)

liist=[]
liist.append(sun)
liist.append(vega)
print(liist)
with open('stars.dat', "w") as s:
	for item in liist:
		s.write("%s\n" % item)
	print('Done')
		
