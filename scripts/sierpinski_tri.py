import pygame
import math
import sys

class Sierp:

		
	def __init__(self,a,b,c, color):
		self.left = a
		self.top = b
		self.right = c
		self.color = color
		
	def display(self, surface):
		pygame.draw.polygon(surface, self.color, [self.left, self.top, self.right], 0)

	def baseTop(self):
		return self.top
	
	def midLeft(self):
		end = self.midBase()
		
		x = self.left[0]+ .5*(end[0]-self.left[0]) + (end[1]-self.left[1])*math.sin(math.radians(60))
		y = self.left[1]+ .5*(end[1]-self.left[1]) - (end[0]-self.left[0])*math.sin(math.radians(60))
		
		return (x,y)
	
	def midRight(self):	
		length = (self.right[0]-self.left[0])/2
		return (self.midLeft()[0]+length, self.midLeft()[1])
	
	def baseLeft(self):
		return self.left
	
	def midBase(self):
		length = (self.right[0]-self.left[0])/2
		return (self.left[0]+length, self.left[1])
	
	def baseRight(self):
		return self.right
	
def draw(surface, lines):
	[k.display(surface) for k in lines]
	
def generate(lines, surface):
	next = []
	
	for t in lines:
		a = t.baseLeft()
		b = t.baseTop()
		c = t.baseRight()
		d = t.midLeft()
		e = t.midRight()
		f = t.midBase()
		print(a)
		print(b)
		print(c)
		print(d)
		print(e)
		print(f)
		next.append(Sierp(a,d,f, (255,255,255)))
		next.append(Sierp(d,b,e, (255,255,255)))
		next.append(Sierp(f,e,c, (255,255,255)))
		
		Sierp(d, f, e, (0,0,0)).display(surface)
		
	
	return next
def setup(w,h,it):
	surf = pygame.Surface((w,h))

	lines = []
	start = (0,h)
	end = (w, h)
	
	
	x = start[0]+ .5*(end[0]-start[0]) + (end[1]-start[1])*math.sin(math.radians(60))
	y = start[1]+ .5*(end[1]-start[1]) - (end[0]-start[0])*math.sin(math.radians(60))
	
	lines.append(Sierp(start, (x,y), end, (0,0,0)))
	
	for i in range(it):
		temp = generate(lines, surf)
		lines = temp
	draw(surf, lines)
	pygame.image.save(surf, str(it)+"_iteration_sierpinski_triangle.png")


width = input("Enter a width: ")
height = input("Enter a height: ")
iter = input("Number of iterations: ")
setup(int(width), int(height), int(iter)) 