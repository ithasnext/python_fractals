import pygame
import sys

def setup(w,h,l):
	surf = pygame.Surface((w,h))
	cantor((w-l)/2, h/2, l, surf)
	
	pygame.image.save(surf, str(l)+"_len_line_fractal.png")

def cantor(x,y,length, surface):
	pygame.draw.line(surface, (255,255,255), (x,y), (x+length, y))
	pygame.draw.line(surface, (255,255,255), (x,y-length/2), (x, y+length/2))
	pygame.draw.line(surface, (255,255,255), (x+length/2,y-length/2), (x+length/2, y+length/2))
	
	if length >= 5:
		cantor(x,y+length/2, length/2, surface)
		cantor(x,y-length/2, length/2, surface)
		cantor(x+length,y+length/2, length/2, surface)
		cantor(x+length,y-length/2, length/2, surface)
		
width = input("Enter a width: ")
height = input("Enter a height: ")
length = input("Enter a length: ")
setup(int(width), int(height), int(length)) 