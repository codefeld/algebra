import slope
from fractions import Fraction

def apply_polynomial(coefficients, x):
	value = 0
	for i in range(len(coefficients)):
		c = coefficients[i]
		p = c * (x**i)
		value += p
	return value

if __name__ == "__main__":
	o = int(input("Enter degree: "))
	coefficients = []
	constant = Fraction(input("Enter constant: "))
	coefficients.append(constant)
	print("Enter coefficients: ")
	r = range(o)
	for i in r:
		c = Fraction(input("  x^{}: ".format(i + 1)))
		coefficients.append(c)
	print("Enter interval: ")
	x1 = Fraction(input("  Start: "))
	x2 = Fraction(input("  Finish: "))
	y1 = apply_polynomial(coefficients, x1)
	y2 = apply_polynomial(coefficients, x2)
	print()
	print("points: ({}, {}), ({}, {})".format(x1, y1, x2, y2))
	s = slope.find_slope(x1, y1, x2, y2)
	print("average rate of change = {}".format(s))