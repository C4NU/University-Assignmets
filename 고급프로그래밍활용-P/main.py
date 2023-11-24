n = int(input())

n1 = int(input())
n2 = int(input())
n3 = int(input())

file_name = input()

data = []

for i in range(0, n):
	name = input()

	kor = input()
	math = input()
	eng = input()
	
	sum = str(int(kor) * (n1 / 100) + int(math) * (n2/100) + int(eng) * (n3/100))

	data.append([name, kor, math, eng, sum])

with open(file_name, 'w+') as file:
	for num, i in enumerate(data):
		if num+1 < len(data):
			file.write(', '.join(i) + "\n")
		else:
			file

temp = []

with open(file_name, "r") as file:
	for fi in file:
		ll = [ name.strip() for name in fi.split(",")]
		temp.append(ll)

temp.sort(key=lambda x:x[4])

print(temp)
for i in range(0, n):
	print(f"{temp[i][0]} {float(temp[i][4]):.1f}")