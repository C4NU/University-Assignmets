n = int(input())

data = []
data_2 = []

for i in range(0, n):
	temp = int(input())
	if data.__contains__(temp):
		continue
	else:
		data.append(temp)

for i in range(0, len(data)):
	for j in range(i, len(data)):
		if data[i] > data[j]:
			temp = data[i]
			data[i] = data[j]
			data[j] = temp
		
print(f"Up = {data}")

for i in range(len(data)-1, -1, -1):
	data_2.append(data[i])

print(f"Down = {data_2}")

final = []
for i in range(0, len(data)):
	final.append(data[i] + data_2[i])

print(f"Final = {final}")