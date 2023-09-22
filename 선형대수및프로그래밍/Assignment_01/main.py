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

# 파일 경로 기반으로 읽어오는 read_file 함수
def read_file(file_path):
	# 데이터 편집을 위한 flag 변수
	matrix_input_flag = False
	operation_input_flag = False

	# 반복문에서 파일 line 별 index로 활용하는 변수
	i = 0
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

	while i < len(lines):
		# 각 줄을 공백을 기준으로 나눠서 필요한 정보 추출
		line = lines[i].strip()
		parts = line.strip().split()

		# 입력 데이터중 공백 처리
		if not parts:
			i += 1
			continue

		# 입력 문장 첫 단어가 "Matrix" 일 때
		elif parts[0] == "Matrix":
			if parts[1] == "수:":
				matrix_input_size = int(parts[2])
				i += 1
			elif parts[1] == "정보:":
				matrix_input_flag = True
				i += 1

		# 입력 문장 첫 단어가 "연산" 일 때
		elif parts[0] == "연산":
			matrix_input_flag = False

			if parts[1] == "수:":
				operation_time = int(parts[2])
				i += 1
			elif parts[1] == "정보:":
				operation_input_flag = True
				i += 1

		else:
			# 행렬 입력 플래그가 True 일때
			if matrix_input_flag == True:
				# 행렬 입출력 시작
				while matrix_index < matrix_input_size:
					# 행렬 dictionary에 데이터 삽입 위한 변수 초기화
					matrix_info = lines[i].strip().split()
					matrix_name = matrix_info[0]
					matrix_size = (int(matrix_info[1]), int(matrix_info[2]))
					matrix_data = []
					# 행렬 2차원 배열 삽입
					for j in range(i + 1, i + 1 + matrix_size[0]):
						matrix_data.append(list(map(int, lines[j].strip().split())))
						matrices[matrix_name] = {
						"size": matrix_size,
						"data": matrix_data
					}
					
					i += matrix_size[0] + 2
					matrix_index += 1

			if operation_input_flag == True:
				# 연산 정보를 읽어서 처리
				operation_line = lines[i].strip().split()
				
				# 연산 명령어가 Add / Mul / Minus 일때는 2개를 입력받아 처리
				if operation_line[0] == "Add" or operation_line[0] == "Mul" or operation_line[0] == 'Minus':
					operation_name = operation_line[0]
					operation_val_count = operation_line[1]
					matrix1_name = operation_line[2]
					matrix2_name = operation_line[3]
					operations.append(operation_name+" "+operation_val_count+" "+matrix1_name+" "+matrix2_name)
					
				# 연산 명령어가 Trace 일 때는 행렬 하나만 입력받아 처리
				elif operation_line[0] == "Trace":
					operation_name = operation_line[0]
					matrix_name = operation_line[1]
					operations.append(operation_name+" "+matrix1_name)
				
				else:
					# 지원하지 않는 연산일 경우 처리
					print(f"Unsupported operation: {operation_line[0]}")
				
				i += 1

	# 데이터 처리된 행렬 및 연산 명령어 반환
	return matrices, operations

def calculation(matrices, operations, file_path):
	f = open(file_path, 'w')
	# 연산 횟수 저장
	operation_index = len(operations)
	# 행렬 데이터 갯수 저장
	matrices_index = len(matrices)
	index = 0

	while index < operation_index:
		# 연산 명령어 쪼개기
		operation_parts = operations[index].split()

		if operation_parts[0] == 'Add':
			# 행렬 덧셈 연산 후 저장
			try:
				# 행렬 1, 2 각각 크기 저장
				matrix_1_size = matrices[operation_parts[2]]['size']
				matrix_2_size = matrices[operation_parts[3]]['size']

				# 행렬 1, 2 각 각 배열 정보 저장
				matrix_1 = matrices[operation_parts[2]]['data']
				matrix_2 = matrices[operation_parts[3]]['data']

				# 결과값 행렬 초기화
				matrix_result = [[0 for j in range(matrix_1_size[1])] for i in range(matrix_1_size[0])]

				# 행렬에 더하여 삽입
				for i in range(matrix_1_size[0]):
					for j in range(matrix_1_size[1]):
						matrix_result[i][j] = matrix_1[i][j] + matrix_2[i][j]

				# 연산 명령어 저장
				operation_result = operation_parts[0] + " " + operation_parts[2] + " " + operation_parts[3]
				
				# 파일에 연산 명령어 출력
				f.write(operation_result + "\n")
				
				# 파일에 행렬 출력
				for i in range(len(matrix_result)):
					for j in range(len(matrix_result)):
						f.write(str(matrix_result[i][j]) + " ")
					f.write("\n")
			except:
				# 문제발생시 예외처리
				print("Add 명령어 연산 정보 불량.")

		elif operation_parts[0] == 'Minus':
			# 행렬 뺄셈 연산 후 저장
			try:
				# 행렬 1, 2 각각 크기 저장
				matrix_1_size = matrices[operation_parts[2]]['size']
				matrix_2_size = matrices[operation_parts[3]]['size']
				
				# 행렬 1, 2 각 각 배열 정보 저장
				matrix_1 = matrices[operation_parts[2]]['data']
				matrix_2 = matrices[operation_parts[3]]['data']

				# 결과값 행렬 초기화
				matrix_result = [[0 for j in range(matrix_1_size[1])] for i in range(matrix_1_size[0])]

				# 행렬에 뺄셈한 후 삽입
				for i in range(matrix_1_size[0]):
					for j in range(matrix_1_size[1]):
						matrix_result[i][j] = matrix_1[i][j] - matrix_2[i][j]

				# 연산 명령어 저장
				operation_result = operation_parts[0] + " " + operation_parts[2] + " " + operation_parts[3]
				
				# 파일에 명령어 출력
				f.write(operation_result + "\n")
				
				# 파일에 행렬 출력
				for i in range(len(matrix_result)):
					for j in range(len(matrix_result)):
						f.write(str(matrix_result[i][j]) + " ")
					f.write("\n")
			except:
				# 연산 명령어 오류시 예외 처리
				print("Minus 명령어 연산 정보 불량.")

		elif operation_parts[0] == 'Mul':
			# 행렬 곱셈 연산 후 저장
			try:
				# 가져온 행렬의 크기와 데이터
				matrix_1_size = matrices[operation_parts[2]]['size']
				matrix_2_size = matrices[operation_parts[3]]['size']
				matrix_1 = matrices[operation_parts[2]]['data']
				matrix_2 = matrices[operation_parts[3]]['data']

				# 결과 행렬의 크기 초기화 (행렬 곱셈 규칙에 따라 설정)
				result_rows = matrix_1_size[0]
				result_cols = matrix_2_size[1]
				matrix_result = [[0 for _ in range(result_cols)] for _ in range(result_rows)]

				# 행렬 곱셈 수행
				for i in range(result_rows):
					for j in range(result_cols):
						for k in range(matrix_1_size[1]):  # 또는 matrix_2_size[0]을 사용해도 됩니다.
							matrix_result[i][j] += matrix_1[i][k] * matrix_2[k][j]

				# 연산 결과를 파일에 쓰기
				operation_result = operation_parts[0] + " " + operation_parts[2] + " " + operation_parts[3]
				f.write(operation_result)
				f.write("\n")
				for i in range(result_rows):
					for j in range(result_cols):
						f.write(str(matrix_result[i][j]) + " ")
					f.write("\n")
			except:
				print("행렬 곱셈 명령어 연산 정보 불량.")


		elif operation_parts[0] == 'Trace':
			# 행렬 Trace (대각합) 연산 후 저장
			matrix_size = matrices[operation_parts[1]]['size']
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
	input_file_path = "input03.txt"
	# 파일을 출력할 경로와 파일명
	output_file_path = "output03.txt"

	# 행렬 (dictionary) / 연산 명령어 (list) 를 파일에서 읽어옴.
	matrices, operations = read_file(file_path=input_file_path)

	# 행렬 및 연산 명령어를 참조하여 연산 후 파일에 출력함.
	calculation(matrices=matrices,
			 operations=operations,
			 file_path=output_file_path)
	

# main으로 실행될 때 main 함수 실행
if __name__ == "__main__":
	main()
