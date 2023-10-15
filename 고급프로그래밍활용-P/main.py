n = int(input())

for _ in range(n, 0, -1):
	for i in range(0, (n-_)):
		print(" ", end="")
	for j in range(0, _ * 2 - 1):
		print("*", end="")
	
	print("")