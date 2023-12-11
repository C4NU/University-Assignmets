'''
도서관 재고 관리 프로그램을 작성하고자 한다. 이 프로그램은 다음과 같은 기능을 가지고 있다.
- 도서관에 새로운 책을 추가하거나 기존 책의 수량을 업데이트 할 수 있다.
- 모든 책의 목록과 각각의 수량을 출력할 수 있다.
- 특정 책의 수량을 조회할 수 있다.

먼저 'books'라는 이름의 딕셔너리를 사용하여, '#'이 입력될때까지 도서의 이름과 수량을 순서대로 입력받는다.
이후 특정 도서의 이름을 입력받으면 전체 책의 목록 및 수량과 해당 책의 수량을 출력하는 프로그램을 작성하시오.

[입력 예시1]
python
5
c
3
java
2
#
python

[출력 예시1]
python : 5
c : 3
java : 2
Quantity of 'python' : 5

[입력 예시2]
python
5
c
3
python
2
java
4
c
1
#
c

[출력 예시2]
python : 7
c : 4
java : 4
Quantity of 'c' : 4
'''

books = dict()

while True:
	book_name = input()

	if book_name == '#':
		break
	else:
		book_numbers = int(input())

		if book_name in books:
			books[book_name] += book_numbers
		else:
			books[book_name] = book_numbers

book_name = input()

for keys in books.keys():
	print(f"{keys} : {books[keys]}")

print(f"Quantity of '{book_name}' : {books[book_name]}")