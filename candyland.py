import itertools
from random import shuffle
import time
import copy

player_count = 4
color_map = {
	"r":"red",
	"p":"purple",
	"y":"yellow",
	"b":"blue",
	"o":"orange",
	"g":"green"}
bridge_1 = (5,59)
bridge_2 = (34,47)
sticky_spaces = [48, 86, 121]
jump_spaces = [9,18,43,75,96,104]
board = "_rpybogrp1ybogrpyb2ogrpybogrpybogrpybogrpyb3ogrpybogrpybogrpybogrpybogrpybo4grpybogrpybogrpybogr5pybogrp6ybogrpybogrpybogrpybogrpybogrp*"
cards = ["r","rr","g","gg","o","oo","b","bb","y","yy","p","pp","0","1","2","3","4","5"]

def init_deck():
	deck = [
		[cards[0]]*6+
		[cards[1]]*4+
		[cards[2]]*6+
		[cards[3]]*3+
		[cards[4]]*6+
		[cards[5]]*3+
		[cards[6]]*6+
		[cards[7]]*4+
		[cards[8]]*6+
		[cards[9]]*4+
		[cards[10]]*6+
		[cards[11]]*4+
		[cards[12]]+
		[cards[13]]+
		[cards[14]]+
		[cards[15]]+
		[cards[16]]+
		[cards[17]]][0]

	shuffle(deck)
	return deck

def player_turn(player_id, deck, player_pos):
	pos = player_pos[player_id]
	card = deck.pop()
	if(pos in sticky_spaces):
		# print("stuck "+str(pos))
		if board[pos] in card:
			# print("unstuck "+card)
			for char in card:
				pos=get_next_color(pos, char)
	elif card in "012345":
		pos = jump_spaces[int(card)];
		# print("jump "+str(pos))
	else:
		for char in card:
			pos=get_next_color(pos, char)
	if pos == bridge_1[0]: 
		pos=bridge_1[1]
	if pos == bridge_2[0]: 
		pos=bridge_2[1]
	player_pos[player_id]=pos

def get_next_color(pos, color):
	if pos==135:
		return pos
	if color not in board[pos+1:]:
		pos = 135
	else:
		# print(board[pos+1:board[pos+1:].index(color)+1+pos])
		pos = board[pos+1:].index(color)+pos+1
	return pos

def run_game(player_count):
	deck = init_deck()
	player_pos = [0] * player_count
	current_player = player_count-1
	turn_list = []
	while 135 not in player_pos:
		current_player=(current_player+1)%(player_count)
		card = deck[-1]
		player_turn(current_player, deck, player_pos)
		turn_list.append((current_player, card, copy.deepcopy(player_pos)))
		if len(deck)==0:
			deck = init_deck()
	return turn_list

def main():
	turnset = run_game(player_count)
	for turn in turnset:
		print(str(turn[0]) + " draws " + str(turn[1]))
		print(turn[2])
	winner = turnset[-1][2].index(135)
	print("Game over. Winner: "+str(winner))
	print("Total turns: "+str(((len(turnset)-(1+winner))/player_count)+1))

if __name__ == "__main__":
	main()