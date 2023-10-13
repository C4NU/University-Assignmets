input_01 = int(input())
input_02 = int(input())
input_03 = int(input())

if input_01 > input_02:
    if input_01 > input_03:
        if input_02 > input_03:
            second_largest = input_02
        else:
            second_largest = input_03
    else:
        second_largest = input_01
else:
    if input_02 > input_03:
        if input_01 > input_03:
            second_largest = input_01
        else:
            second_largest = input_03
    else:
        second_largest = input_02

sum = input_01 + input_02 + input_03

print(f"The value in the middle is {second_largest}")
if sum % 2 == 0:
	print(f"{sum} is even number")
else:
	if sum % 3 == 0:
		print(f"{sum} is odd number, multiple of 3")
	else:
		print(f"{sum} is odd number, not multiple of 3")