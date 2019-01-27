import pygame
import sys

def setup(w,h,r):
	surf = pygame.Surface((w,h))
	fract_circle(w/2, h/2, r, surf)
	
	pygame.image.save(surf, str(r)+"_radius.png")

# 1 level recursion
def fract_circle(x,y, radius, surface):
	if radius > 1:
		pygame.draw.circle(surface, (0,0,255), (int(x),int(y)), int(radius), 1)
	if radius > 2:
		radius *= .75
		fract_circle(x,y,radius,surface)
		
width = input("Enter a width: ")
height = input("Enter a height: ")
radius = input("Enter a radius: ")

setup(int(width), int(height), int(radius)) 