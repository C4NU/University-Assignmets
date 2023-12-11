'''
사용자로부터 각 줄마다 학생의 번호와 이름을 1개의 공백을 두고 한 줄로 입력받으며' #'을 입력 받으면 입력 받는 것을 종료한다.
이후 입력 받은 각 사용자별로 대여 기록을 입력받으며 '#'을 입력 받으면 입력 받는 것을 종료한다. 
대여기록을 입력받을때는, 사용자 이름과 책 이름을 1개의 공백을 두고 한줄로 입력받으며 이때 책 이름에는 공백이 포함되지 않는다.
마지막으로 대여 기록을 확인할 학생의 이름을 입력받고, 입력받은 학생이 대여한 책 이름을 출력하는 프로그램을 작성하시오.
(단, 대여기록이 없을때는 "Not Found"를 출력한다.)

[입력 예시1]
1 Liam
2 Emma
3 Noah
#
Liam HarryPotter
Emma AnimalFarm
Noah TheGreatGatsby
#
Liam

[출력 예시1]
HarryPotter

[입력 예시2]
24 Ava
37 Mia
2 Jack
10 Lucy
#
Ava Dracula
Lucy Alchemist
Mia 1984
Jack Beloved
#
Ethan

[출력 예시2]
Not Found

[입력 예시3]
10 Chloe
30 Ryan
20 Grace
40 Max
50 Lily
70 Luke
60 Anna
#
Lily Jaws
Grace 1984
Chloe Nineteen
Anna Matilda
Ryan Hamlet
Max Frankenstein
#
Ryan

[출력 예시3]
Hamlet
'''

student = dict()

while True:
	input_str = input()

	if input_str == '#':
		break
	else:
		input_str = input_str.split(' ')

		student_number = input_str[0]
		student_name = input_str[1]

		student_data = list()
		student_data.append(student_number)

		student[student_name] = student_data

while True:
	input_str = input()

	if input_str == '#':
		break

	else:
		input_str = input_str.split(' ')

		student_name = input_str[0]
		student_borrowed = input_str[1]

		student_data = student[student_name]
		student_data.append(student_borrowed)

		student[student_name] = student_data

name = input()

try:
	print(f'{student[name][1]}')
except:
	print('Not Found')
