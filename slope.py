def find_slope(x1, y1, x2, y2):
	rise = y2 - y1
	run = x2 - x1
	m = rise / run
	return m

def find_y_int(x1, y1, x2, y2):
	m = find_slope(x1, y1, x2, y2)
	b = y1 - (m * x1)
	return b

if __name__ == "__main__":
	p1 = [0, 10]
	p2 = [5, 35]
	print("slope: %s" % find_slope(p1[0], p1[1], p2[0], p2[1]))
	print("y-intercept: %s" % find_y_int(p1[0], p1[1], p2[0], p2[1]))
