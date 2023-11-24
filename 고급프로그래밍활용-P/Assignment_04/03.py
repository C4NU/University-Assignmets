'''
지출 목록을 만들어 주는 프로그램을 만들고자 한다.
먼저 사용자는 지출 내역 문자열과 지출액(0 보다 큰 정수)을 입력한다.
만약 지출 내역 문자열을 입력하는 단계에서 'exit'을 입력하면, 입력 받기를 중단한다.

이후 입력이 모두 끝나면, 모든 지출 내역과 지출액을 동시에 출력하고,
다음으로 가장 큰 비용을 지출한 지출 내역과 지출액을 따로 출력한다.
(단, 유효한 입력은 최소 한 번 이상 등록된다고 가정하며 최대 지출액은 단 하나로 결정된다고 가정한다. 또한 모든 지출 내역과 지출액 출력시 띄어쓰기 없이 "지출내역:지출액" 형태로 출력하지만 가장 큰 비용을 지출한 지출 내역과 지출액을 출력할 때는 "Maximum Expense: 지출내역,지출액" 형태로 띄어쓰기에 유의한다.)

[입력 예시 1]
rent
500000
electricity
30000
water
50000
exit

[출력 예시 1]
rent:500000
electricity:30000
water:50000
Maximum Expense: rent,500000

[입력 예시 2]
insurance
10000
transportation
40000
phone bill
30000
exit

[출력 예시 2]
insurance:10000
transportation:40000
phone bill:30000
Maximum Expense: transportation,40000
'''

usage_dict = dict()

while True:
	usage = input()

	if usage == 'exit':
		break

	transaction = int(input())

	usage_dict[usage] = transaction

max = 0
max_key = 0

for i in usage_dict.keys():
	print(f"{i}:{usage_dict[i]}")

	if max < usage_dict[i]:
		max = usage_dict[i]
		max_key = i

print(f"Maximum Expense: {max_key},{usage_dict[max_key]}")
	

