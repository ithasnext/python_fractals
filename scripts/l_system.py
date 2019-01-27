import pygame
import MutableString
import math

width = input("Enter a width: ")
height = input("Enter a height: ")
length = input("Enter a length: ")
iterations = input("Enter the number of iterations: ")
angle = input("Enter the angle of branches: ")
random = input("Allow random branch numbers: ")
setup(int(width), int(height), int(length), int(iterations), angle, random)


# An LSystem has a starting sentence
# An a ruleset
# Each generation recursively replaces characteres in the sentence
# Based on the rulset

class LSystem():
	  # Construct an LSystem with a startin sentence and a ruleset
	  __init__(self, axiom, r):
	    self.sentence = axiom
	    self.ruleset = r
	    self.generation = 0

	  # Generate the next generation
	  def generate(self):
	  	# An empty StringBuffer that we will fill
	  	nextgen = MutableString()
	  	# For every character in the sentence
	  	for curr in sentence:
	  		# We will replace it with itself unless it matches one of our rules
	  		replace = "" + curr
	  		# Check every rule
	  		for j in ruleset:
	  			a = j.a
	  			# if we match the Rule, get the replacement String out of the Rule
	  			if (a == curr):
	  				replace = j.b
	  				break
	  		# Append replacement String
	  		nextgen.append(replace);
	  	# Replace sentence
	  	sentence = str(nextgen)
	  	# Increment generation
	  	generation += 1

class Rule():
	__init__(self, partA, partB):
		self.a = partA
		self.b = partB
