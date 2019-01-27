import pygame
import sys

def setup(w,h,l):
	surf = pygame.Surface((w,h))
	cantor(50, 100, l, surf)
	
	pygame.image.save(surf, str(l)+"_len_cantor_line.png")

def cantor(x,y,length, surface):
	pygame.draw.line(surface, (255,255,255), (x,y), (x+length, y))
	y += 20
	if length >= 1:
		cantor(x,y, length/3, surface)
		cantor(x + (length*2/3), y, length/3, surface)
	
width = input("Enter a width: ")
height = input("Enter a height: ")
length = input("Enter a length: ")
setup(int(width), int(height), int(length)) 