n = int(input())

list_data = list()

for i in range(0, n):
	list_data.append(int(input()))

s = int(input())
e = int(input())


temp_list = list()

for i in range(s, e+1):
	for j in range(s, i+1):
		temp_list.append(list_data[j])
	print(temp_list)
	temp_list = list()




