import math

def i_power(exponent):
	x = math.remainder(exponent, 4)
	if x == 0:
		return 1 + 0j
	elif x == 1:
		return 1j
	elif x == 2:
		return -1 + 0j
	elif x == 3:
		return -1j
	else:
		raise("ERROR...ERROR...NOT A NUMBER...SYSTEM OVERLOAD")

if __name__ == "__main__":
	e = int(input("Please enter the exponent: "))
	print(i_power(e))
