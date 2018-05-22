import candyland
import math

player_count = 4
def game_len(game):
	return math.ceil(len(game)/player_count)

def get_winner(game):
	return game[-1][0]

def get_player_draws(game, player):
	draws = []
	for turn in game:
		if(turn[0]==player):
			draws.append(turn[1])
	return draws

game_set = []
for i in range(10000):
	game = candyland.run_game(player_count)
	game_set.append(game)

avg_len = list(map(game_len, game_set))
avg_len = sum(avg_len)/len(avg_len)
print("Average game length: "+str(avg_len))

winner_dist = [0,0,0,0]
for game in game_set:
	winner_dist[get_winner(game)]+=1
print("Winner distribution: ")
print("{:>5} {:>5} {:>5} {:>5}".format("0","1","2","3"))
print("{:>5} {:>5} {:>5} {:>5}".format(winner_dist[0]*100/sum(winner_dist), winner_dist[1]*100/sum(winner_dist), winner_dist[2]*100/sum(winner_dist), winner_dist[3]*100/sum(winner_dist)))

winner_drew_4_count = 0
winner_drew_5_count = 0
winner_drew_jump_count = [0]*6
for game in game_set:
	winner_draws = get_player_draws(game, get_winner(game))
	if "4" in winner_draws:
		winner_drew_jump_count[4]+=1
	if "5" in winner_draws:
		winner_drew_jump_count[5]+=1
print("Winner drew jump 4 in {}% of games".format(winner_drew_jump_count[4]*100/len(game_set)))
print("Winner drew jump 5 in {}% of games".format(winner_drew_jump_count[5]*100/len(game_set)))