import pygame
import math
from random import randint
import sys

class Branch():

	def __init__(self, a, b, c, w):
		self.start = a
		self.end = b
		self.weight = w
		if c == "true":
			self.angle = randint(2,20)
			self.rand = True
		elif c !="0":
			self.angle = int(c)
			self.rand = False
		else:
			self.angle = 4
			self.rand = False

	def show(self, surface):
		pygame.draw.line(surface, (255,255,255), self.start, self.end, int(self.weight))
	def rad_angle(self):
		return math.pi/self.angle

	def branch(self):

		vect = ((self.end[0] - self.start[0])*.66, (self.start[1] - self.end[1])*.66)
		dirX = math.cos(math.pi/self.angle) * vect[0] + math.sin(math.pi/self.angle) * vect[1]
		dirY = -math.sin(math.pi/self.angle) * vect[0] + math.cos(math.pi/self.angle) * vect[1]
		a = self.angle
		if self.rand == True:
			a = "true"
		left = Branch(self.end, (self.end[0] + dirX, self.end[1] - dirY), a, self.weight* .66)

		dirX = math.cos(-math.pi/self.angle) * vect[0] + math.sin(-math.pi/self.angle) * vect[1]
		dirY = -math.sin(-math.pi/self.angle) * vect[0] + math.cos(-math.pi/self.angle) * vect[1]

		right = Branch(self.end, (self.end[0] + dirX, self.end[1] - dirY),a, self.weight* .66)

		return (left, right)


	def branch_random(self):

		vect = ((self.end[0] - self.start[0])*.66, (self.start[1] - self.end[1])*.66)
		a = self.angle
		if self.rand == True:
			a = "true"

		# 1 = left, 2 = right, 3 = both
		numBranch = randint(1,3)
		branches = []
		if numBranch == 3 or numBranch == 1:
			dirX = math.cos(math.pi/self.angle) * vect[0] + math.sin(math.pi/self.angle) * vect[1]
			dirY = -math.sin(math.pi/self.angle) * vect[0] + math.cos(math.pi/self.angle) * vect[1]

			left = Branch(self.end, (self.end[0] + dirX, self.end[1] - dirY), a, self.weight* .66)
			branches.append(left)
		if numBranch == 2 or numBranch == 3:
			dirX = math.cos(-math.pi/self.angle) * vect[0] + math.sin(-math.pi/self.angle) * vect[1]
			dirY = -math.sin(-math.pi/self.angle) * vect[0] + math.cos(-math.pi/self.angle) * vect[1]

			right = Branch(self.end, (self.end[0] + dirX, self.end[1] - dirY),a, self.weight* .66)

			branches.append(right)

		return branches


	#left branch
	#x = end[0]+ .5*(nEnd[0]-end[0]) + (nEnd[1]-end[1])*math.sin(math.pi/4)
	#y = end[1]+ .5*(nEnd[1]-end[1]) - (nEnd[0]-end[0])*math.sin(math.pi/4)

	#pygame.draw.line(surface, (255,255,255), end, (x,y))

	#right branch
	#x = end[0]+ .5*(nEnd[0]-end[0]) + (nEnd[1]-end[1])*math.sin(-math.pi/4)
	#y = end[1]+ .5*(nEnd[1]-end[1]) - (nEnd[0]-end[0])*math.sin(math.pi/4)
	#pygame.draw.line(surface, (255,255,255), end, (x,y))


def draw(surface, tree):
	[t.show(surface) for t in tree]


def setup(w,h,l,i, a, r):
	surf = pygame.Surface((w,h))

	x = pygame.Surface.get_width(surf)/2
	y = pygame.Surface.get_height(surf)

	root = Branch((x,y), (x,y-l), a, 20)
	tree = [root]


	it = 0
	for it in range(i):
		for t in range(len(tree)):
			if r != "true":
				[tree.append(b) for b in tree[t-1].branch()]
			else:
				[tree.append(b) for b in tree[t-1].branch_random()]
	draw(surf, tree)
	pygame.image.save(surf, str(i)+"_it_deter_tree.png")

	#pygame.draw.line(surface, (255,255,255), (x+length/2,y-length/2), (x+length/2, y+length/2))

width = input("Enter a width: ")
height = input("Enter a height: ")
length = input("Enter a length: ")
iterations = input("Enter the number of iterations: ")
angle = input("Enter the angle of branches: ")
random = input("Allow random branch numbers: ")
setup(int(width), int(height), int(length), int(iterations), angle, random)
