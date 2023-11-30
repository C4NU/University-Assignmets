def main():
    # 자연수 n 입력
    n = int(input())

    # 파일 이름 및 형식 입력
    file_name = input()

    # 단어 입력 및 파일에 저장
    with open(file_name, 'w') as file:
        for i in range(n):
            word = input()
            file.write(word + '\n')

    # 파일 불러와서 정렬
    sorted_words = load_and_sort_words(file_name)

    # 정렬된 결과 출력
    print("\n정렬된 결과:")
    for word in sorted_words:
        print(word)

def load_and_sort_words(file_name):
    # 파일 불러오기
    with open(file_name, 'r') as file:
        words = [line.strip() for line in file]

    # 중복 제거를 위해 집합으로 변환 후 다시 리스트로 변환
    unique_words = list(set(words))

    # 길이가 짧은 것부터 정렬, 길이가 같으면 사전 순으로 정렬
    sorted_words = sorted(unique_words, key=lambda x: (len(x), x))

    return sorted_words

if __name__ == "__main__":
    main()
