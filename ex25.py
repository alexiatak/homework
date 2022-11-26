class Star:
	def __init__(self, absmag):
		self.absmag = absmag
	def __repr__(self):
		return f"{self.absmag}"
		
def find_cluster_magnitude(stars,pc):
	import math
	for star in stars:
		s = 0
		s = s + 10**(-0.4*(star.absmag))
		sabsolute = -2.5*(math.log10(s))
		sapparent= sabsolute + 5 - 5*(math.log10(pc))
	return sapparent
sun=Star(4.8)
vegas=Star(0.58)
sirius=Star(1.4)
stars=()
stars=(sun,vegas,sirius)
res=find_cluster_magnitude(stars,4)
print(res)
liist=sorted(stars, key = lambda x: x.absmag)
print(liist)
