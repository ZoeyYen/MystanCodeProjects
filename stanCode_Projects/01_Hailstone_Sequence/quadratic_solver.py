"""
File: quadratic_solver.py
Name:Zoey
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	print the roots of equation :  ax^2 + bx + c = 0
	"""
	print('stanCode Quadratic Solver!')
	a = float(input('Enter a: '))
	b = float(input('Enter b: '))
	c = float(input('Enter c: '))
	discriminant = b*b-4*a*c
	if discriminant > 0:
		y = math.sqrt(discriminant)
		x1 = (-1*b+y)/2/a
		x2 = (-1*b-y)/2/a
		print('Two roots: '+str(x1)+' , '+str(x2))
	elif discriminant == 0:
		x = -1*b/2/a
		print('One root: '+str(x))
	else:
		print('No real roots')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
