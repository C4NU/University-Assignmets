# 18010714 전효재 과제 2

def init_output_file(file_path):
	f = open(file_path, 'w')
	f.close()
# 파일 경로 기반으로 읽어오는 read_file 함수
def read_file(file_path):
	# 반복문에서 파일 line 별 index로 활용하는 변수
	index = 0
	# 저장할 행렬 변수 (dictionary)
	matrices = {}
	# 행렬 dictionary에 데이터 삽입할 때 사용하는 index 변수
	matrix_index = 0

	# 파일을 읽어서 lines 리스트에 저장
	with open(file_path, 'r', encoding= 'utf-8') as file:
		lines = file.readlines()

	while index < len(lines):
		# 각 줄을 공백을 기준으로 나눠서 필요한 정보 추출
		line = lines[index].strip()
		parts = line.strip().split()
		
		# 입력 데이터중 공백 처리
		if not parts or parts[0] == "#":
			index += 1
			continue
		
		# 입력 문장 첫 단어가 "Matrix" 일 때
		elif parts[0] == "Matrix":
			if parts[1] == "수:":
				matrix_input_size = int(parts[2])
				index += 1

		else:
			# 행렬 입출력 시작
			while matrix_index < matrix_input_size:
				# 행렬 dictionary에 데이터 삽입 위한 변수 초기화
				matrix_info = lines[index].strip().split()
				matrix_name = matrix_index
				matrix_size = (int(matrix_info[0]), int(matrix_info[1]))
				matrix_data = []
				# 행렬 2차원 배열 삽입 (n:m 비율로 수정해야함)
				# matrix_size[0]: 행 (row)
				# matrix_size[1]: 열 (col)

				for j in range(index + 1, index + 1 + matrix_size[1]):
					matrix_data.append(list(map(int, lines[j].strip().split())))
					matrices[matrix_name] = {
					"size": matrix_size,
					"data": matrix_data
					}
				
				index += matrix_size[1] + 2
				matrix_index += 1

	# 데이터 처리된 행렬 및 연산 명령어 반환
	return matrices

def calc_determinant(matrix):
	# Cofactor Expansion 사용해서 Determinant 계산하는 함수
	# matrix 저장된 정보 값
	# matrix_name: 행렬 이름
	# matrix_size: 행렬 크기 (N, M) 사이즈
	# matrix_size: 행렬 정보

	# 정방행렬이 아닐때
	if matrix['size'][0] != matrix['size'][1]:
		print("Unsupported Calculation: Not Square Matrix")
		return None
	
	else:
		# 행렬 크기가 1 by 1 일때
		if matrix['size'][0] == matrix['size'][1] == 1:
			return matrix['data'][0][0]
		
		# 행렬 크기가 2 by 2 일때
		elif matrix['size'][0] == matrix['size'][1] == 2:
			return matrix['data'][0][0] * matrix['data'][1][1] - matrix['data'][1][0] * matrix['data'][0][1]
		
		# 행렬 크기가 3 by 3 이상 일때
		else:
			det = 0

			for col in range(matrix['size'][1]):
				sub_matrix = []

				for i in range(1, matrix['size'][0]):
					sub_row = []
					for j in range(matrix['size'][1]):
						if j != col:
							sub_row.append(matrix['data'][i][j])
					sub_matrix.append(sub_row)
				sub_det = calc_determinant(sub_matrix)

				if col % 2 == 0:
					det += matrix[0][col] * sub_det
				else:
					det -= matrix[0][col] * sub_det
			
			return det

def calc_cofactor_matrix(matrix):
	# Cofactor Matrix 계산하는 함수
	pass

def print_matrix(matrix):
	for i in range(0, matrix['size'][1]):
		for j in range(0, matrix['size'][0]):
			print(str(matrix['data'][i][j])+" ", end="")
		print("")
	
	print("")

def main():
	# 파일을 읽어올 경로와 파일명
	input_file_path = "input.txt"
	# 파일을 출력할 경로와 파일명
	output_file_path = "output.txt"

	index = 0
	
	init_output_file(output_file_path)

	# 행렬 (dictionary)을 파일에서 읽어옴
	matrices = read_file(file_path=input_file_path)
	
	while index < len(matrices):
		#print_matrix(matrices[index])
		determinant = calc_determinant(matrices[index])
		cofactor_matrix = calc_cofactor_matrix(matrices[index])

		print(f"det(행렬): {determinant}")
		index += 1

# main으로 실행될 때 main 함수 실행
if __name__ == "__main__":
	main()
