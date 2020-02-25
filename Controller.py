import math
import random
import re
import sys, os

from Board import Board
from Player import Player
from Ai import Ai
from View import View

class Controller:
    ROW_COUNT = 6
    COLUMN_COUNT = 7
    game_board = Board(ROW_COUNT, COLUMN_COUNT)
    view = View()
    players = []
    current_player = None
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
            ###########################
            ### Player vs. Computer ###
            if game_mode == 2:
                for idx in range(player_count):
                    self.players.append(self.register_player(idx))
                self.players.append(self.register_ai(idx +1))
            #############################
            ### Computer vs. Computer ###
            if game_mode == 3:
                for idx in range(player_count):
                    self.players.append(self.register_ai(idx))
    
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
            self.game_board.add_chip(column, player.chip_id +1)
            self.view.show_board(self.game_board.get_board())
            return True
        else:
            self.view.show_message('invalid move')
            return False

    def initialize_new_game(self):
        self.game_board = Board(self.ROW_COUNT, self.COLUMN_COUNT)
        self.players = []
        self.current_player = None
        self.turn = 0
        self.start_game()

    def game_is_running(self, game_mode):
        self.initialize_players(game_mode)
        self.view.show_board(self.game_board.get_board())

        while self.running_game:
            self.get_active_player()
            if self.players[self.current_player].type == 'human':
                player_input = self.view.player_input(self.players[self.current_player].name)
            else:
                player_input = int(random.uniform(1, self.COLUMN_COUNT +1))
            
            if type(player_input) is int: 
                self.handle_player_move(self.players[self.current_player], player_input -1)
                # TODO modify winning move to check for draw
                if self.game_board.winning_move(self.current_player +1):
                    self.view.winning_player(self.players[self.current_player])
                    ########################
                    ### start a new game ###
                    self.initialize_new_game()

    #################################
    ### This method runs the game ###
    def start_game(self):
        self.view.start_screen()
        game_mode = self.view.init_game_mode()
        reg_ex = re.search('[1-3]', game_mode)

        ###########################
        ### Run a specific game ###
        if reg_ex and len(game_mode) == 1:
            self.game_is_running(int(game_mode))

        #################
        ### Exit Game ###
        if int(game_mode) == 4:
            sys.exit()

        else:
            print('wrong input')
            self.start_game()