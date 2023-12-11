def palindrom(string):

	for _ in range(0, int(len(string) / 2)):
		
		if(string[_] != string[len(string)-_-1]):
			return False
		
	return True

times = int(input())

result = 0

for _ in range(0, times):
	string = input()

	if palindrom(string):
		result += 1

print(result)