win = 0
draw = 0
lose = 0

n = int(input())
player_input = input()

for _ in range(0, n):
	enemy_input = input()

	if player_input == 's' or player_input == 'S':
		if enemy_input == 'r' or enemy_input == 'R':
			lose += 1
		elif enemy_input == 's' or enemy_input == 'S':
			draw += 1
		elif enemy_input == 'p' or enemy_input =='P':
			win += 1

	elif player_input == 'r' or player_input == 'R':
		if enemy_input == 'r' or enemy_input == 'R':
			draw += 1
		elif enemy_input == 's' or enemy_input == 'S':
			win += 1
		elif enemy_input == 'p' or enemy_input =='P':
			lose += 1

	elif player_input == 'p' or player_input == 'P':
		if enemy_input == 'r' or enemy_input == 'R':
			win += 1
		elif enemy_input == 's' or enemy_input == 'S':
			lose += 1
		elif enemy_input == 'p' or enemy_input =='P':
			draw += 1

print(f"Win: {win}")
print(f"Draw: {draw}")
print(f"Lose: {lose}")