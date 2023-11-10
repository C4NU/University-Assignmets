'''
자연수 n을 입력받고 각 자릿수에 대해
홀수의 개수와 짝수의 개수를 계산하여 출력하는 프로그램을 작성하라.
(단, 자릿수에 0은 없다고 가정한다.)

[입력 예시1]
512		--> 5와 1은 홀수, 2는 짝수

[출력 예시1]
The odd number is 2
The even number is 1

[입력 예시2]
42874		--> 4,2,8,4는 짝수, 7은 홀수

[출력 예시2]
The odd number is 1
The even number is 4
'''

n = int(input())

max_digit = 1

odd = 0
even = 0

while True:
	if int(n / max_digit) == 0:
		max_digit /= 10
		break
	else:
		max_digit *= 10

while n > 1:
	temp = int(n / max_digit)

	if temp % 2 == 0:
		even += 1
	else:
		odd += 1

	n = int(n % max_digit)
	max_digit /= 10

print(f"The odd number is {odd}")
print(f"The even number is {even} ")

