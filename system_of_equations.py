import math

def solve_elimination(a, b, c, d, e, f):
	'''ax + by = c, dx + ey = f'''
	# 1. Multiply the first equation by d and the second equation by -a
	#    This will eliminate x when we add the equations.
	#    This will create gy = h, iy = j
	#    I am done now
	g = d * b
	h = d * c
	i = -a * e
	j = -a * f
	if g == -i and h == -j:
		return math.nan, math.nan, "infinite solutions"

	# 2. Add the equations to solve for y
	#    This will create y = l/k
	k = g + i
	l = h + j
	if k == 0:
		return math.nan, math.nan, "no solutions"
	y = l / k

	# 3. Substitute y to solve for x
	n = b * y
	o = c - n
	x = o / a
	return x, y, ""

def _print_solution(x, y, e):
	if len(e) != 0:
		print("  %s" % e)
	else:
		print("  x = %s" % x)
		print("  y = %s" % y)

if __name__ == "__main__":
	print("\n20x - 5y = 5\n4x - y = 1")
	x, y, e = solve_elimination(20, -5, 5, 4, -1, 1)
	_print_solution(x, y, e)

	print("\n5x - y = 2\n5x - y = -2")
	x, y, e = solve_elimination(5, -1, 2, 5, -1, -2)
	_print_solution(x, y, e)

	print("\n6x + 3y = 9\n6x + y = 9")
	x, y, e = solve_elimination(6, 3, 9, 6, 1, 9)
	_print_solution(x, y, e)