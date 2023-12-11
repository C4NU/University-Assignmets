def print_2darray(array):
	for i in range(0, len(array)):
		for j in range(0, len(array[i])):
			print(array[i][j], end = ' ')
		print()

n = int(input())

array = [[0] * n for _ in range(n)]

for i in range(0, n):
	for j in range(0, n):
		array[i][j] = int(input())

array2 = [[0] * n for _ in range(n)]
for i in range(0, n):
	for j in range(0, n):
		array2[i][j] = array[n - j - 1][i]

print_2darray(array2)

array3 = [[0] * n for _ in range(n)]
for i in range(0, n):
	for j in range(0, n):
		array3[i][j] = array[j][n - i - 1]

print_2darray(array3)

array4 = [[0] * n for _ in range(n)]
for i in range(0, n):
	for j in range(0, n):
		array4[i][j] = array2[i][j] + array3[i][j]
print_2darray(array4)