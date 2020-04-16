############
### TODO ###

### Controller.py ###

# - Build debug mode log.txt (AI Moves chosed columns + score)

# - Build debug array [
# column, -80
# column, 6000
# column, 0
# ]

#


### Board.py ###

#


### Ai.py ###

#


### player.py ###

#


### View.py ###

# 



    # ###############
    # ### MiniMax ###
    # def is_terminal_node(self):
    #     return self.game_board.winning_move(self.players[self.current_player].chip_id +1) or self.game_board.winning_move(self.opponent_chip) or len(self.game_board.get_valid_locations(self.column_count)) == 0

    # def minimax(self, game_board, depth, max_player):
    #     valid_locations = game_board.get_valid_locations(self.column_count)
    #     is_terminal = self.is_terminal_node()

    #     if is_terminal:
    #         if game_board.winning_move(self.players[self.current_player].chip_id +1):
    #             return None, 100000000000
    #         elif game_board.winning_move(self.opponent_chip):
    #             return None, -100000000000
    #         else:
    #             return None, 0
    #     if depth == 0:
    #         return None, self.score_position(game_board, self.players[self.current_player].chip_id +1)
        
    #     if max_player:
    #         value = -math.inf
    #         best_column = random.choice(valid_locations)

    #         for column in valid_locations:
    #             tmp_game_board = copy.deepcopy(game_board)
    #             self.add_chip(column, tmp_game_board, self.players[self.current_player].chip_id +1)
    #             new_score = self.minimax(tmp_game_board, depth -1, False)[1]
    #             if new_score > value:
    #                 value = new_score
    #                 best_column = column
    #                 # print('player: ', self.players[self.current_player].chip_id +1,' Depth: ', depth,' Best Column:', best_column, ' value: ', value,)
    #                 # time.sleep(0.3)
    #         return best_column, value

    #     else:
    #         value = math.inf
    #         best_column = random.choice(valid_locations)

    #         for player in range(len(self.players)):
    #             if self.players[player].type  != 'machine':
    #                 for column in valid_locations:
    #                     tmp_game_board = copy.deepcopy(game_board)
    #                     self.add_chip(column, tmp_game_board, self.players[player].chip_id +1)
    #                     new_score = self.minimax(tmp_game_board, depth -1, True)[1]
    #                     if new_score < value:
    #                         value = new_score
    #                         best_column = column
    #                         # print('player: ', self.opponent_chip,' Depth: ', depth,' Best Column:', best_column, ' value: ', value,)
    #                         # time.sleep(0.3)
    #         return best_column, value

