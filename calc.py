import random
def make_puetion():
	x = random.randint(1,100)
	y = random.randint(1,100)
	giho = random.randint(1,3)
	if giho == 1:
		giho = '+'
	elif giho == 2:
		giho = '-'
	elif giho == 3:
		giho = '*'
	quetion = str(x) + giho + str(y)
	return quetion
	
