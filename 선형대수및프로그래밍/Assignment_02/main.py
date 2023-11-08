# 18010714 전효재 과제 2

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

	matrix_data = matrix['data']
	num_rows, num_cols = len(matrix_data), len(matrix_data[0])
	
	# 정방행렬이 아닐때
	if num_rows != num_cols:
		print("Unsupported Calculation: Not Square Matrix")
		return None
	
	else:
		# 행렬 크기가 1 by 1 일때
		if num_rows == num_cols == 1:
			return matrix_data[0][0]
		
		# 행렬 크기가 2 by 2 일때
		elif num_rows == num_cols == 2:
			return matrix_data[0][0] * matrix_data[1][1] - matrix_data[0][1] * matrix_data[1][0]
		
		# 행렬 크기가 3 by 3 이상 일때
		else:
			det = 0

			for col in range(num_cols):
				sub_matrix_data = []

				for i in range(1, num_rows):
					sub_row_data = []
					for j in range(num_cols):
						if j != col:
							sub_row_data.append(matrix_data[i][j])
					sub_matrix_data.append(sub_row_data)
				sub_matrix_dict = {"data": sub_matrix_data}
				sub_det = calc_determinant(sub_matrix_dict)

				if col % 2 == 0:
					det += matrix_data[0][col] * sub_det
				else:
					det -= matrix_data[0][col] * sub_det
		return det

def calc_cofactor_matrix(matrix):
	# Cofactor Matrix 계산하는 함수
	matrix_data = matrix["data"]
	num_rows, num_cols = len(matrix_data), len(matrix_data[0])
	cofactor_data = []

# 행렬 크기가 1 by 1 일때
	if num_rows == num_cols == 1:
		return matrix_data[0][0]
	
	else:
		for i in range(num_rows):
			cofactor_row = []
			for j in range(num_cols):
				sub_matrix_data = []
				for row in range(num_rows):
					if row != i:
						sub_row = []
						for col in range(num_cols):
							if col != j:
								sub_row.append(matrix_data[row][col])
						sub_matrix_data.append(sub_row)
				sub_matrix_dict = {"data": sub_matrix_data}
				sub_det = calc_determinant(sub_matrix_dict)
				cofactor_element = (-1) ** (i + j) * sub_det
				cofactor_row.append(cofactor_element)
			cofactor_data.append(cofactor_row)

		return {"data": cofactor_data}

def print_matrix(matrix, f, var):
	# 입력받은 행렬을 출력할 때
	if var == 0:	
		f.write(str(matrix['size'][0]) + " " + str(matrix['size'][1]) + "\n")
		for i in range(0, matrix['size'][1]):
			for j in range(0, matrix['size'][0]):
				f.write(str(matrix['data'][i][j])+" ")
			f.write("\n")
		
		f.write("\n")
	# Cofactor Matrix 연산 수행 후 출력할 때
	if var == 1:
		if type(matrix) is dict:
			num_row, num_col = len(matrix['data'][0]), len(matrix['data'][1])

			for i in range(0, num_col):
				for j in range(0, num_row):
					f.write(str(matrix['data'][i][j])+" ")
				f.write("\n")

			f.write("\n")
		else:
			f.write(str(matrix)+"\n\n")

def main():
	# 파일을 읽어올 경로와 파일명
	input_file_path = "input01.txt"
	# 파일을 출력할 경로와 파일명
	output_file_path = "output01.txt"

	index = 0
	
	f = open((output_file_path), 'w')
	
	# 행렬 (dictionary)을 파일에서 읽어옴
	matrices = read_file(file_path=input_file_path)
	
	while index < len(matrices):
		print_matrix(matrices[index], f, 0)

		determinant = calc_determinant(matrices[index])
		f.write(str(determinant)+"\n\n")

		cofactor_matrix = calc_cofactor_matrix(matrices[index])
		print_matrix(cofactor_matrix, f, 1)

		index += 1

# main으로 실행될 때 main 함수 실행
if __name__ == "__main__":
	main()
