from math import sqrt

def quad(a, b, c):
	d = (b**2) - (4 * a * c)
	if d < 0:
		print("No Solution")
	else:
		e = (-b + sqrt(d)) / (2 * a)
		f = (-b - sqrt(d)) / (2 * a)
		print("%s, %s" % (e, f))

def vertex(a, b, c):
	x = -b / (2 * a)
	y = (a * (x**2)) + (b * x) + c

	print("x = %s" % x)
	print("y = %s" % y)

if __name__ == "__main__":
	vertex(1, 0, 0)