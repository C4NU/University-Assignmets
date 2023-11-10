'''
자연수 n을 입력받고,
예시와 같이 *로 다이아몬드 형태를 출력하는 프로그램을 작성하시오.

[입력 예시 1]
3

[출력 예시 1]
  *
 ***
*****
 ***
  *

[입력 예시 2]
5

[출력 예시 2]
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

n = int(input())

for i in range(1, n+1):
	for j in range(n-i, 0, -1):
		print(" ", end="")
	for k in range(0, i * 2 -1):
		print("*", end="")
	print("")

for i in range(n-1, 0, -1):
	for j in range(n-i, 0, -1):
		print(" ", end="")
	for k in range(0, i * 2 -1):
		print("*", end="")
	print("")