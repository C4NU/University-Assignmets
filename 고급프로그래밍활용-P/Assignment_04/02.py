'''
사용자가 도서관에 책을 모두 정리했을 때, 
모음으로 시작하는 책과 자음으로 시작하는 책을 분리하여 보관하려고 합니다. 
1. 책의 갯수를 입력 받는다.
2. 각 책의 이름을 순서대로 입력 받는다. 
3. 입력 받은 순서대로 자음으로 시작하는 책의 이름과 모음으로 시작하는 책의 이름을 따로 저장한다.
4. 자음으로 시작하는 책과 모음으로 시작하는 책을 입력 받은 순서대로 출력하는 프로그램을 작성하라. 

단, 책의 이름은 영어 소문자로만 입력 받는다.
리스트에 아무 값이 없으면, "[]"로 출력이 된다.


[입력 예시 1]
5
apple
banana
grape
orange
watermelon

[출력 예시 1]
consonant: ['banana', 'grape', 'watermelon']
vowel: ['apple', 'orange']

[입력 예시 2]
4
book
umbrella
dictionary
encyclopedia

[출력 예시 2]
consonant: ['book', 'dictionary']
vowel: ['umbrella', 'encyclopedia']
'''

def check_vowels(char):
	if char == 'a' or char == 'i' or char == 'e' or char == 'o' or char == 'u':
		return True
	else:
		return False
	
n = int(input())

consonant = list()
vowel = list()

for i in range(0, n):
	book_name = input()
	
	if check_vowels(book_name[0]):
		vowel.append(book_name)
	else:
		consonant.append(book_name)

print(f"consonant: {consonant}")
print(f"vowel: {vowel}")
