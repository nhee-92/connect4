import math
import random
import re
import sys
import time
import copy

from Board import Board
from Player import Player
from Ai import Ai
from View import View

class Controller:
    DEFAULT_ROW_COUNT = 6
    DEFAULT_COLUMN_COUNT = 7
    row_count = DEFAULT_ROW_COUNT
    column_count = DEFAULT_COLUMN_COUNT
    view = View()
    players = []
    current_player = None
    opponent_chip = None
    running_game = True
    turn = 0

    def register_player(self, id):
        return Player(id, input('Bitte den Namen von Spieler eingeben '))

    def register_ai(self, id):
        return Ai(id)

    def initialize_players(self, game_mode):
        player_count = int(input('Wie viele wollen denn Zocken? '))

        if type(player_count) is int:
            self.turn = int(random.uniform(0, player_count +1))
            #########################
            ### Player vs. Player ###
            if game_mode == 1:
                for idx in range(player_count):
                    self.players.append(self.register_player(idx))
                self.view.clear_console()
            ###########################
            ### Player vs. Computer ###
            if game_mode == 2:
                for idx in range(player_count):
                    self.players.append(self.register_player(idx))
                self.players.append(self.register_ai(idx +1))
                self.view.clear_console()
            #############################
            ### Computer vs. Computer ###
            if game_mode == 3:
                for idx in range(player_count):
                    self.players.append(self.register_ai(idx))
                self.view.clear_console()
    
    def get_active_player(self):
        if self.current_player == None:
            self.current_player = self.players[self.turn-1].chip_id
        else:
            self.current_player = self.change_active_player().chip_id

    def change_active_player(self):
        players_length = len(self.players)

        if self.turn > players_length - 1:
            self.turn = 0

        for idx in range(players_length):
            self.players[idx].active = False

        #TODO Schleife entfernen
        for idx in range(players_length):
            if idx == self.turn:
                self.turn += 1
                self.players[idx].active = True
                return self.players[idx]

    def handle_player_move(self, player, column):
        if self.game_board.is_position_free_in_column(column):
            self.add_chip(column, self.game_board, player.chip_id +1)
            self.view.clear_console()
            self.view.connect_four()
            self.view.enter_help()
            self.view.show_board(self.game_board.get_board())
            return True
        else:
            self.view.show_message('invalid move')
            return False

    def add_chip(self, column, game_board, chip):
        if game_board.is_position_free_in_column(column):
            game_board.board[game_board.get_next_open_row(column)][column] = chip


    #######################
    ### Control KI Move ###
    def evaluate_score(self, window, chip):
        score = 0

        if window.count(chip) == 4:
            score += 100
        elif window.count(chip) == 3 and window.count(0) == 1:
            score += 10
        elif window.count(chip) == 2 and window.count(0) == 2:
            score += 5

        if self.opponent_chip != None:
            if window.count(self.opponent_chip) == 3 and window.count(0) == 1:
                score -= 80

        return score

    def score_position(self, game_board, chip):
        score = 0

        ####################
        ### Score Center ###
        center_arr = [int(i) for i in list(game_board.board[:, self.column_count // 2])]
        center_count = center_arr.count(chip)
        score += center_count * 6

        ########################
        ### Horizontal Score ###
        for row in range(self.row_count):
            row_arr = [int(i) for i in list(game_board.board[row,:])]
            for column in range(self.column_count -3):
                window = row_arr[column:column +4]
                score += self.evaluate_score(window, chip)
        
        ######################
        ### Vertical Score ###
        for column in range(self.column_count):
            column_arr = [int(i) for i in list(game_board.board[:,column])]
            for row in range(self.row_count -3):
                window = column_arr[row:row +4]
                score += self.evaluate_score(window, chip)

        ##############################
        ### Positiv Diagonal Score ###
        for row in range(self.row_count -3):
            for column in range(self.column_count -3):
                window = [game_board.board[row +i][column +i] for i in range(4)]
                score += self.evaluate_score(window, chip)

        ###############################
        ### Negative Diagonal Score ###
        for row in range(self.row_count -3):
            for column in range(self.column_count -3):
                window = [game_board.board[row +3-i][column +i] for i in range(4)]
                score += self.evaluate_score(window, chip)

        return score

    def get_best_move(self, game_board, chip):
        valid_locations = self.game_board.get_valid_locations(self.column_count)
        best_score = -10000
        best_column = random.choice(valid_locations)
        
        for column in valid_locations:
            tmp_game_board = copy.deepcopy(self.game_board)
            self.add_chip(column, tmp_game_board, chip +1)
            score = self.score_position(tmp_game_board, chip +1)

            if score > best_score:
                best_score = score
                best_column = column +1

        return best_column
    ### End KI Move ###
    ###################

    def reset_game(self):
        self.game_board = Board(self.row_count, self.column_count)
        self.players = []
        self.current_player = None
        self.turn = 0
        self.start_application()

    def start_game(self, game_mode):
        self.initialize_players(game_mode)
        self.view.connect_four()
        self.view.enter_help()
        self.game_board = Board(self.row_count, self.column_count)
        self.view.show_board(self.game_board.get_board())

        while self.running_game:
            self.get_active_player()
            if self.players[self.current_player].type == 'human':
                self.opponent_chip = self.players[self.current_player].chip_id +1
                player_input = self.view.player_input(self.players[self.current_player].name)
            elif self.players[self.current_player].type == 'machine':
                player_input = self.get_best_move(self.game_board, self.players[self.current_player].chip_id)
            
            if type(player_input) is int:
                self.handle_player_move(self.players[self.current_player], player_input -1)
                if self.game_board.winning_move(self.current_player +1):
                    self.view.winning_player(self.players[self.current_player])
                    time.sleep(3)
                    ##########################
                    ### reset current game ###
                    self.reset_game()

    #################################
    ### This method runs the game ###
    def start_application(self):
        self.view.clear_console()
        self.view.connect_four()
        self.view.start_screen()
        game_mode = self.view.init_game_mode()
        reg_ex = re.search('[1-3]', game_mode)

        ###########################
        ### Run a specific game ###
        if reg_ex and len(game_mode) == 1:
            self.start_game(int(game_mode))

        ####################
        ### Game Options ###
        if int(game_mode) == 4:
            self.view.clear_console()
            self.view.connect_four()
            self.view.options_screen()

            option_input = int(input())

            if option_input == 1:
                self.view.clear_console()
                self.view.connect_four()
                self.view.option_change_gameboard(self.DEFAULT_ROW_COUNT, self.DEFAULT_COLUMN_COUNT)
                self.row_count = int(input('Rows: '))
                self.column_count = int(input('Columns: '))
            
            if option_input == 2:
                self.start_application()

        #################
        ### Exit Game ###
        if int(game_mode) == 5:
            sys.exit()

        else:
            print('wrong input')
            self.start_application()