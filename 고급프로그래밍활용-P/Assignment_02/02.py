print("Answer: ", end="")
answer = int(input())

count = 0

while True:
	print("Guess: ", end="")
	guess = int(input())

	count += 1
	if guess > 100 or guess < 1:
		print("Out of range")
	else:
		if guess > answer:
			print("DOWN")
		elif guess < answer:
			print("UP")
		else:
			print("CORRECT")
			break

print(count)