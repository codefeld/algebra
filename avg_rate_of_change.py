import slope

def apply_polynomial(coefficients, x):
	value = 0
	for i in range(len(coefficients)):
		c = coefficients[i]
		p = c * (x**i)
		print("%d * %d ^ %d = %d" % (c, x, i, p))
		#print("%d * %d = %d" % (c, (x**i), p))
		value += p
	return value

if __name__ == "__main__":
	o = int(input("Enter order: "))
	coefficients = []
	constant = int(input("Enter constant: "))
	coefficients.append(constant)
	print("Enter coefficients: ")
	r = range(1, o)
	for i in r:
		c = int(input("  x^%d: " % i))
		coefficients.append(c)
	print("Enter interval: ")
	x1 = int(input("  Start: "))
	x2 = int(input("  Finish: "))
	y1 = apply_polynomial(coefficients, x1)
	y2 = apply_polynomial(coefficients, x2)
	print()
	print("points: (%d, %d), (%d, %d)" % (x1, y1, x2, y2))
	s = slope.find_slope(x1, y1, x2, y2)
	print("average rate of change = %d" % s)