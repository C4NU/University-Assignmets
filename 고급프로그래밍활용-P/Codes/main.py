male_age_sum = 0
female_age_sum = 0

oldest_sex = 'm'
oldest_age = 0

for i in range(0, 5):
	input_sex = input()
	input_age = int(input())

	if input_sex == 'm':
		male_age_sum += input_age
	else:
		female_age_sum += input_age

	if oldest_age < input_age:
		oldest_age = input_age
		oldest_sex = input_sex

if male_age_sum >= female_age_sum:
	print(f"m {male_age_sum}")
else:
	print(f"f {female_age_sum}")

print(f"{oldest_sex} {oldest_age}")
