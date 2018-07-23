
def print_scores(game_score_dict, player1, player2):
	print("Current Score")
	print('-'*len("Current Score"))
	ab="Set"+' '*max(len(player1),len(player2))+'    '+'1'+'  '+'2'+'  '+'3'
	player1_scores = game_score_dict[1][player1], game_score_dict[2][player1], game_score_dict[3][player1]
	player2_scores = game_score_dict[1][player2], game_score_dict[2][player2], game_score_dict[3][player2]

	print("Set{:>10}{:>12}{:>14}".format(1,2,3))
	print('-'*len(ab))
	print("{}{:>10}{:>12}{:>14}".format(player1, player1_scores[0],player1_scores[1],player1_scores[2]))
	print("{}{:>10}{:>12}{:>14}".format(player2, player2_scores[0],player2_scores[1],player2_scores[2]))
	

def decide_winner(game_score_dict, player1, player2):
	player1_scores = game_score_dict[1][player1], game_score_dict[2][player1], game_score_dict[3][player1]
	player2_scores = game_score_dict[1][player2], game_score_dict[2][player2], game_score_dict[3][player2]

	score_diff = sum([1 if x-y > 0 else 0 for x,y in zip(player1_scores, player2_scores)])
	if score_diff >=2 :
		print("Match over. %s wins!" %(player1))
	else:
		print("Match over. %s wins!" %(player2))

#Enter the player name
player1 = input("Enter the name of player 1: ")
player2 = input("Enter the name of player 2: ")

set_count=1
game_score_dict = {1:{player1:0, player2:0}, 2:{player1:0, player2:0}, 3:{player1:0, player2:0}}
while set_count != 4:

	set_on = True
	player1_game_score=0
	player2_game_score=0

	while set_on:
		# Set win condition
		if player2_game_score >= 6 or player1_game_score >= 6:
			if player1_game_score - player2_game_score >= 2:
				set_count += 1
				# TODO Print set scores
				print("Set Over")
				set_on = False				
				break
			elif player2_game_score - player1_game_score >= 2:
				set_count += 1
				# TODO Print set scores
				print("Set Over")
				set_on = False
				break

		first_serve = int(input("Who starts the first serve? (1 for %s, 2 for %s): " %(player1,player2)))
		if first_serve == 1:
			pass
		elif first_serve == 2:
			pass
		
		input("Waiting for the game to start (HIT ENTER) ")

		player1_score=0
		player2_score=0
		game_on = True

		while game_on:
			#Match is won by first/second player
			if player1_score >= 40 and player2_score >= 40:
				#Score is Deuce
				if player1_score==player2_score:
					print("The score is Deuce")

				#Player in lead has advantage
				if player1_score - player2_score == 10:
					print("%s has Advantage:" %(player1))
				elif player2_score - player1_score == 10:
					print("%s has Advantage:" %(player2))

				#Match Point
				next_point = int(input("Winner of next point (1 for %s, 2 for %s): " %(player1,player2)))
				if next_point==1:
					player1_score += 10
				elif next_point == 2:
					player2_score += 10

				if player1_score - player2_score >= 20:
					print("%s wins the game: " %(player1))
					player1_game_score += 1
					game_on = False
					print("Game over")
					game_score_dict[set_count][player1] = player1_game_score
					#game_score_dict[set_count][player2] = player2_game_score
					print_scores(game_score_dict, player1, player2)

				elif player2_score - player1_score >= 20:
					print("%s wins the game: " %(player2))
					player2_game_score += 1
					game_on = False
					print("Game over")
					#game_score_dict[set_count][player1] = player1_game_score
					game_score_dict[set_count][player2] = player2_game_score
					print_scores(game_score_dict, player1, player2)
			elif player1_score > 40 and player2_score < 40:
				print("%s wins the game: " %(player1))
				player1_game_score += 1
				game_on = False
				print("Game over")
				game_score_dict[set_count][player1] = player1_game_score
				#game_score_dict[set_count][player2] = player2_game_score
				print_scores(game_score_dict, player1, player2)
				
			elif player1_score < 40 and player2_score > 40:
				print("%s wins the game: " %(player2))
				player2_game_score += 1
				game_on = False
				print("Game over")
				#game_score_dict[set_count][player1] = player1_game_score
				game_score_dict[set_count][player2] = player2_game_score
				print_scores(game_score_dict, player1, player2)

			else:
				next_point = int(input("Winner of next point (1 for %s, 2 for %s): " %(player1,player2)))
				if next_point==1:
					if player1_score < 30:
						player1_score += 15
					else:
						player1_score += 10
				elif next_point == 2:
					if player2_score < 30:
						player2_score += 15
					else:
						player2_score += 10
				print("Game score: %d - %d  " %(player1_score,player2_score))

#Match is won by
decide_winner(game_score_dict, player1, player2)

 
















#

