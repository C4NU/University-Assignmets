# Copyright 2023 Hyo Jae Jeon (CANU) canu1832@gmail.com

# 팀원
# 18010714 전효재
# 18011667 신무성
# 20011842 이윤혁
# 21013320 이채린

import math

# list 형태의 데이터를 string으로 편집하여 return 하는 함수
def list_to_string(str_list):
	result = ""
	for str in str_list:
		result += str + " "

	return result.strip()

def init_output_file(file_path):
	f = open(file_path, 'w')
	f.close()

# 파일 경로 기반으로 읽어오는 read_file 함수
def read_file(file_path, i):
	# 데이터 편집을 위한 flag 변수
	matrix_input_flag = False
	operation_input_flag = False

	# 반복문에서 파일 line 별 index로 활용하는 변수
	index = i
	# 저장할 행렬 변수 (dictionary)
	matrices = {}
	# 저장할 연산 명령어 변수 (list) 
	operations =[]

	# 행렬 dictionary에 데이터 삽입할 때 사용하는 index 변수
	matrix_index = 0
	# 연산 명령어 list에 데이터 삽입할 때 사용하는 index 변수
	operation_index = 0

	# 파일을 읽어서 lines 리스트에 저장
	with open(file_path, 'r', encoding= 'utf-8') as file:
		lines = file.readlines()

	while index < len(lines):
		# 각 줄을 공백을 기준으로 나눠서 필요한 정보 추출
		line = lines[index].strip()
		parts = line.strip().split()

		# 연산이 끝나고 새로운 입력을 받을때
		#operation_input_flag가 끝나고 공백을 입력받았을때?
		if operation_input_flag == True and not parts:
			matrix_input_flag = False
			operation_input_flag = False
			return matrices, operations, 1, index
			
		# 입력 데이터중 공백 처리
		if not parts or parts[0] == "#":
			index += 1
			continue

		# 파일 입력 완전 종료일때
		elif parts[0] == "end":
			return matrices, operations, 2, index
		
		# 입력 문장 첫 단어가 "Matrix" 일 때
		elif parts[0] == "Matrix":
			if parts[1] == "수:":
				matrix_input_size = int(parts[2])
				index += 1
			elif parts[1] == "정보:":
				matrix_input_flag = True
				index += 1

		# 입력 문장 첫 단어가 "연산" 일 때
		elif parts[0] == "연산":
			if parts[1] == "수:":
				operation_time = int(parts[2])
				index += 1
			elif parts[1] == "정보:":
				operation_input_flag = True
				index += 1

		else:
			# 행렬 입력 플래그가 True 일때
			if matrix_input_flag == True:
				# 행렬 입출력 시작
				while matrix_index < matrix_input_size:
					# 행렬 dictionary에 데이터 삽입 위한 변수 초기화
					matrix_info = lines[index].strip().split()
					matrix_name = matrix_info[0]
					matrix_size = (int(matrix_info[1]), int(matrix_info[2]))
					matrix_data = []
					# 행렬 2차원 배열 삽입 (n:m 비율로 수정해야함)
					# matrix_size[0]: 행 (row)
					# matrix_size[1]: 열 (col)
					matrix_row = matrix_size[0]
					matrix_col = matrix_size[1]
					for j in range(index + 1, index + 1 + matrix_size[1]):
						matrix_data.append(list(map(int, lines[j].strip().split())))
						matrices[matrix_name] = {
						"size": matrix_size,
						"data": matrix_data
					}
					
					index += matrix_size[1] + 2
					matrix_index += 1

			if operation_input_flag == True:
				# 연산 정보를 읽어서 처리
				operation_line = lines[index].strip().split()
				
				# 연산 명령어가 Add / Mul / Minus 일때는 N개를 입력받아 처리
				if operation_line[0] == "Add" or operation_line[0] == "Mul" or operation_line[0] == 'Minus':
					operation_name = operation_line[0]
					operation_val_count = operation_line[1]

					operation_result = operation_name+" "+operation_val_count+" "

					for _ in range(int(operation_val_count)):
						matrix_name = operation_line[_+2]
						operation_result = operation_result + (matrix_name + " ")
						
					operation_result = operation_result[:-1]
					operations.append(operation_result)

				# 연산 명령어가 Trace 일 때는 행렬 하나만 입력받아 처리
				elif operation_line[0] == "Trace":
					operation_name = operation_line[0]
					matrix_name = operation_line[1]
					operations.append(operation_name+" "+matrix_name)
				
				else:
					# 지원하지 않는 연산일 경우 처리
					print(f"Unsupported operation: {operation_line[0]}")
				
				index += 1
				
	# 데이터 처리된 행렬 및 연산 명령어 반환
	return matrices, operations, 0, index

# 행렬 및 연산 명령어를 참조하여 연산 후 파일에 출력함.
def calculation(matrices, operations, file_path):
	f = open(file_path, 'a')
	# 연산 횟수 저장
	operation_index = len(operations)
	# 행렬 데이터 갯수 저장
	matrices_index = len(matrices)
	index = 0

	while index < operation_index:
		# 연산 명령어 쪼개기
		operation_parts = operations[index].split()
		# DEBUG
		if operation_parts[0] == 'Add':
			# 행렬 덧셈 연산 후 저장
			try:
				operand_count = int(operation_parts[1])
				matrix_1_size = matrices[operation_parts[2]]['size']
				matrix_size_row = matrix_1_size[0]
				matrix_size_col = matrix_1_size[1]

				matrix_result = [[0 for j in range(matrix_size_row)] for i in range(matrix_size_col)]

				for i in range(operand_count):
					matrix_name = operation_parts[i + 2]
					matrix_data = matrices[matrix_name]['data']

					for i in range(matrix_size_col):
						for j in range(matrix_size_row):
							matrix_result[i][j] += matrix_data[i][j]

				# 연산 명령어 저장
				operation_result = ""
				for i in range(len(operation_parts)):
					if i == 1:
						continue
					else:
						operation_result += operation_parts[i] + " "

				# 파일에 연산 명령어 출력
				f.write(operation_result + "\n")
				
				# 파일에 행렬 출력
				for i in range(matrix_size_col):
					for j in range(matrix_size_row):
						f.write(str(matrix_result[i][j]) + " ")
					f.write("\n")
			except:
				# 문제발생시 예외처리
				print("Add 명령어 연산 정보 불량.")
				f.write(f"{operations[index]}: Can not operate Add because incompatible dimensions for standard matrix add." + "\n")

		elif operation_parts[0] == 'Minus':
			# 행렬 뺄셈 연산 후 저장
			try:
				operand_count = int(operation_parts[1])
				matrix_1_size = matrices[operation_parts[2]]['size']
				matrix_size_row = matrix_1_size[0]
				matrix_size_col = matrix_1_size[1]

				matrix_result = [[0 for j in range(matrix_size_row)] for i in range(matrix_size_col)]

				for i in range(operand_count):
					matrix_name = operation_parts[i + 2]
					matrix_data = matrices[matrix_name]['data']
					
					for i in range(matrix_size_col):
						for j in range(matrix_size_row):
							matrix_result[i][j] -= matrix_data[i][j]

				# 연산 명령어 저장
				operation_result = ""
				for i in range(len(operation_parts)):
					if i == 1:
						continue
					else:
						operation_result += operation_parts[i] + " "
				
				# 파일에 명령어 출력
				f.write(operation_result + "\n")
				
				# 파일에 행렬 출력
				for i in range(matrix_size_col):
					for j in range(matrix_size_row):
						f.write(str(matrix_result[i][j]) + " ")
					f.write("\n")
			except:
				# 연산 명령어 오류시 예외 처리
				print("Minus 명령어 연산 정보 불량.")
				f.write(f"{operations[index]}: Can not operate Minus because of incompatible dimensions for standard matrix minus." + "\n")

		elif operation_parts[0] == 'Mul':
			_flag = 0
			# 행렬 곱셈 연산 후 저장
			def multiply(matrix_1, matrix_2):
				result = [[0]*len(matrix_2[0]) for _ in range(len(matrix_1))]
				for i in range(len(matrix_1)): 
					lists = []
					for j in range(len(matrix_2[0])): 
						for k in range(len(matrix_1[0])): 
							result[i][j] += matrix_1[i][k] * matrix_2[k][j]
				return result
			
			try:
				# 가져온 행렬의 크기와 데이터
				operand_count = int(operation_parts[1])
				
				matrix_1 = matrices[operation_parts[2]]['data']
				matrix_2 = matrices[operation_parts[3]]['data']

				matrix_1_row = len(matrix_1)
				matrix_2_col = len(matrix_2[0])
				
				if matrix_1_row == matrix_2_col:
					result = multiply(matrix_1=matrix_1, matrix_2=matrix_2)
				
					if operand_count >= 3:
						for i in range(4, len(operation_parts)):
							matrix = matrices[operation_parts[i]]['data']
						
							matrix_1_row = len(matrix)
							matrix_2_col = len(result[0])

							if matrix_1_row == matrix_2_col:
								result = multiply(matrix_1=result, matrix_2=matrix)
							else:
								f.write(f"{operations[index]}: Can not operate Mul because of Multiply rule violation." + "\n")
								_flag = 1
								break
					
					if _flag == 0:
						# 연산 결과를 파일에 쓰기
						operation_result = ""
						for i in range(len(operation_parts)):
							if i == 1:
								continue
							else:
								operation_result += operation_parts[i] + " "
						f.write(operation_result + "\n")

						for i in range(len(result)):
							for j in range(len(result[0])):
								f.write(str(result[i][j]) + " ")
							f.write("\n")
					
				else:
					f.write(f"{operations[index]}: Can not operate Mul because of Multiply rule violation." + "\n")
					break



			except:
				print("Mul 명령어 연산 정보 불량.")
				f.write(f"{operations[index]}: Can not operate Mul because of Multiply rule violation." + "\n")

		elif operation_parts[0] == 'Trace':
			# 행렬 Trace (대각합) 연산 후 저장
			matrix_size = matrices[operation_parts[1]]['size']

			if matrix_size[0] != matrix_size[1]:
				f.write(f"{operations[index]}: Can not operate Trace, Because of non-Square Matrix.\n")
			else:
				matrix = matrices[operation_parts[1]]['data']

				result = 0

				for i in range(matrix_size[0]):
					for j in range(matrix_size[1]):
						if i == j:
							result = result + matrix[i][j]

				# 명령어를 형태 유지하여 저장할 수 있게 변환
				operation_result = list_to_string(operation_parts)
				f.write(operation_result + "\n" + str(result) + "\n")

		else:
			# 예외처리
			print("잘못된 연산 명령어 입력")
			return
		
		index += 1
		f.write("\n")

	f.close()


def main():
	# 파일을 읽어올 경로와 파일명
	input_file_path = "input.txt"
	# 파일을 출력할 경로와 파일명
	output_file_path = "output.txt"
	
	init_output_file(output_file_path)
	i = 0

	while True:
		# 행렬 (dictionary) / 연산 명령어 (list) 를 파일에서 읽어옴.
		matrices, operations, flag, i= read_file(file_path=input_file_path, i=i)
		if flag == 0 or flag == 1:
			# 연산을 실행할 때
			calculation(matrices=matrices,
					operations=operations,
					file_path=output_file_path)
		else:
			# end signal이 나왔을때
			break
	

# main으로 실행될 때 main 함수 실행
if __name__ == "__main__":
	main()
