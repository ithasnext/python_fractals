import pygame
import math
import sys


class KochLine:
	
	def __init__(self,a,b):
		self.start = a
		self.end = b
		
	def display(self, surface):
		pygame.draw.line(surface, (255,255,255), self.start, self.end);

	def kochA(self):
		return self.start

	def kochB(self):
		return (self.start[0]+(self.end[0] - self.start[0])/3, self.start[1]+(self.end[1] - self.start[1])/3)
	
	def kochC(self):
		a = self.kochB()
		
		xlen = (self.end[0]-self.start[0])/3
		ylen = (self.end[1]-self.start[1])/3
		
		x = self.start[0]+ .5*(self.end[0]-self.start[0]) + ((self.end[1]-self.start[1])*math.sin(math.radians(60)))/3
		y = self.start[1]+ .5*(self.end[1]-self.start[1]) - ((self.end[0]-self.start[0])*math.sin(math.radians(60)))/3
		
		return (x,y)
		#return (self.start[0]+xlen+(xlen*math.sin(math.radians(60))), self.start[1]+xlen+(xlen*math.sin(math.radians(60))))
	def kochD(self):
		return (self.start[0]+(self.end[0] - self.start[0])*2/3, self.start[1]+(self.end[1] - self.start[1])*2/3)
	def kochE(self):
		return self.end


def draw(surface, lines):
	[k.display(surface) for k in lines]
	#k = lines[0]
	#k.display(surface)
	#k = lines[1]
	#k.display(surface)
	#k = lines[2]
	#k.display(surface)
	#k = lines[3]
	#k.display(surface)
	#k = lines[7]
	#k.display(surface)
	#k = lines[5]
	#k.display(surface)
	#k = lines[6]
	#k.display(surface)
	
def generate(lines):
	next = []
	
	for l in lines:
		a = l.kochA()
		b = l.kochB()
		c = l.kochC()
		d = l.kochD()
		e = l.kochE()
		print("a: "+str(a))
		print("b: "+str(b))
		print("c: "+str(c))
		print("d: "+str(d))
		print("e: "+str(e))
		
		next.append(KochLine(a,b))
		next.append(KochLine(b,c))
		next.append(KochLine(c,d))
		next.append(KochLine(d,e))
		
	return next

def setup(w,h,it):
	surf = pygame.Surface((w,h))

	lines = []
	start = (0,h/2)
	end = (w, h/2)

	lines.append(KochLine(start, end))
	
	for i in range(it):
		temp = generate(lines)
		lines = temp
	draw(surf, lines)
	print(str(len(lines)))
	pygame.image.save(surf, str(it)+"_iteration_koch_line.png")

width = input("Enter a width: ")
height = input("Enter a height: ")
iter = input("Number of iterations: ")
setup(int(width), int(height), int(iter)) 