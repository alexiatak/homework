class CelestialObject:
	def __init__(self,ra,dec):
		self.ra=ra
		self.dec=dec
	
	def show_coordinates(self):
		print("the coordinates are ra:" ,self.ra,"and dec:", self.dec)
			
	def upper_culmination(self,lat):
		if self.dec < lat:
			hupper = 90 - lat + self.dec
		else:
			hupper = 90 - self.dec + lat
		return hupper

	def lower_culmination(self, lat):
		hlower = lat + self.dec - 90
		return hlower

class Star(CelestialObject):
	def __init__(self,temp,radius,ra,dec):
		#CelestialObject.__init__(self,temp,radius,ra,dec)
		super().__init__(ra,dec)
		self.temp=temp
		self.radius=radius
		
		tempSun = 5780
		import math
		self.luminosity = ((self.radius)**2)*((self.temp/tempSun)**4)	
		
class Galaxy(CelestialObject):
	def __init__(self,dist,apparent_mag,ra,dec):
		#CelestialObject.__init__(self,dist,apparent_mag,ra,dec)
		super().__init__(ra,dec)		
		self.dist=dist
		self.apparent_mag=apparent_mag
		
		import math
		self.absolute_mag = self.apparent_mag + 5 - 5*(math.log10(dist*(10**6)))

andromeda=Galaxy(0.7,3.4,ra=20,dec=30)
sirius=Star(9.940,-1.33,ra=60,dec=55)

print(andromeda.absolute_mag)
print(sirius.luminosity)
print(sirius.lower_culmination(60))
print(sirius.upper_culmination(20))
print(andromeda.show_coordinates())
