import math
import numpy as np
import scipy.integrate

def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	n2 = n

	if n < 0:
		raise ValueError("Le nombre ne peut pas être négatif.")
	
	if n == 0:
		return 1
	
	while n > 1:
		n2 = n2*(n-1)
		n = n-1
	return n2
	
	

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	delta = b**2 - 4*a*c

	if delta > 0:
		root1 = (- b + math.sqrt(delta))/(2*a)
		root2 = (- b - math.sqrt(delta))/(2*a)
		return (root1, root2)

	if delta < 0:
		raise ValueError("Le delta n'admet aucune solution.")
	
	if delta == 0:
		root = (- b)/(2*a)
		return (root)

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""	

	if lower > upper:
		raise ValueError("La borne du dessous doit être égale ou plus petite que la borne du dessus.")

	def f(x):
		return eval(function, {"x": x, "np": np})
	
	result, error = scipy.integrate.quad(f, lower, upper)

	return result
	

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
