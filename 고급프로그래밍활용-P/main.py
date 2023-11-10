def spell_check(a):
	if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
		return True
	else:
		return False

n = int(input())

input_list = list()

consonant = list()
vowel = list()

for _ in range(0, n):
	input_list.append(input())

	if spell_check(input_list[_]):
		vowel.append(input_list[_])
	else:
		consonant.append(input_list[_])

for _ in range(1, n+1):
	try:
		if _ % 2 == 1:
			print(consonant.pop(0), end="")
		else:
			print(vowel.pop(0), end="")
	except IndexError:
		if _ % 2 == 1:
			print(vowel.pop(0), end="")
		else:
			print(consonant.pop(0), end="")

