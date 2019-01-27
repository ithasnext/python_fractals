import pygame
import math
import sys

def setup(w, h=0):
	if h == 0:
		surf = pygame.Surface((w, w))
	else:
		surf = pygame.Surface((w, h))
	return surf
	
def create_mod(surface, r, m, n):
	if n > 0:
		spacing  = 360/n
	else:
		spacing = 'err'
	
	if spacing != 'err':
		origin = (surface.get_width()/2, surface.get_height()/2)
		
		points = [(origin[0] + r * math.cos(math.radians(spacing * x)), origin[1] + r * math.sin(math.radians(spacing * x))) for x in range(n)]
	
		[pygame.draw.line(surface, (0,255,0), points[i], points[((i+1) * m) % n]) for i in range(len(points))]
	 
	
	
	
def blow_mind(w, h, r, m, n):
	if h > 0 and r > 0:
		surf = setup(w, h)
		create_mod(surf,r, m, n) 
		pygame.image.save(surf, str(n)+"_points_times_"+str(n)+".png")
		
		
width = input("Enter a width: ")
height = input("Enter a height: ")
radius = input("Enter a radius: ")
multiplier = input("Enter a multipler: ")
num = input("Enter the number of points: ")

blow_mind(int(width), int(height), int(radius), int(multiplier), int(num))