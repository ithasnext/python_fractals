import tkinter
import turtle

def rectangle(start, h, l):
	top = "+"
	mid = "+"
	stop = 0
	while(stop < l):
		top += "+"
		if stop == l-1:
			mid += "+"
		else:
			mid += " "
		stop += 1
		
	print(top)
	stop = 0
	while(stop < h):
		print(mid)
		stop += 1
	print(top)
	
def smoothRect(w,l):
	corner = "+"
	v = "|"
	h = "-"
	
	top = corner
	mid = v
	while(len(top) < l-1):
		top += h
		mid += "~"
	top += corner
	mid += v
	print(top)
	prints = 0
	while(prints < w):
		print(mid)
		prints +=1
	print(top)
	
print("Sweet Hacus")

rectangle(0,4,4)
smoothRect(5,14)
