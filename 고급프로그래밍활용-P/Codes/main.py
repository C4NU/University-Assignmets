r = int(input())
g = int(input())
b = int(input())

if r > 0:
	if g > 0:
		if b > 0:
			print('white')
		else:
			print('yellow')
	else:
		if b > 0:
			print('magenta')
		else:
			print('red')
else:
	if g > 0:
		if b > 0:
			print('cyan')
		else:
			print('green')
	else:
		if b > 0:
			print('blue')
		else:
			print('black')