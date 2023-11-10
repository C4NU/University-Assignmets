'''
주사위 3개를 던졌을때,
세 주사위의 중앙에 위치하는 값을 구하고,
세 주사위의 합을 구하여 합이 홀수이면 합이 홀수라고 출력한 후 3의 배수인지도 판별하여 출력하고 
짝수이면 합이 짝수라고 출력하는 프로그램을 작성하라.
(주사위의 눈은 6이하의 자연수이므로, 1부터 6을 제외한 다른 수의 입력은 제외한다.)

[입력 예시 1]
1
2
3

[출력 예시 1]
The value in the middle is 2
6 is even number

[입력 예시 2]
3
4
6

[출력 예시 2]
The value in the middle is 4
13 is odd number, not multiple of 3

[입력 예시 3]
1
1
1

[출력 예시 3]
The value in the middle is 1
3 is odd number, multiple of 3

[입력 예시 4]
1
5
2

[출력 예시 4]
The value in the middle is 2
8 is even number
'''
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