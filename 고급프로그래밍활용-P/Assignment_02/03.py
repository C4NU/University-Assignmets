americano = 4500
green_tea = 4000
latte = 5000

sum = 0

for i in range(0, 10):
	str_input = input()

	if str_input == 'americano':
		sum += americano
	elif str_input == 'green tea':
		sum += green_tea
	elif str_input == 'latte':
		sum += latte
	elif str_input == '-':
		pass

print(sum)
