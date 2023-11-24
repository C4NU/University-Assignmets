'''
[입력 예시1]
10010111101

[출력 예시1]
32232333323

[입력 예시2]
11100001110101

[출력 예시2]
33322223332323
'''

n = input()

result = n.split('0')
result = '2'.join(result)

result = result.split('1')
result = '3'.join(result)

print(result)