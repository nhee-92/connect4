import re
import os
import time

from Colors import Colors

class View:
    ##########################
    ### Breite der Konsole ###
    terminal_width = os.get_terminal_size().columns

    def connect_four(self):
        print('')
        print((f'{Colors.FAIL}          #######  ########  #       #  #       #  ########  ########  ########  #{Colors.ENDC}        ').center(self.terminal_width))
        print((f'{Colors.FAIL}          #        #      #  # #     #  # #     #  #         #            #      #{Colors.ENDC}        ').center(self.terminal_width))
        print((f'{Colors.FAIL}          #        #      #  #  #    #  #  #    #  #         #            #      #   #{Colors.ENDC}    ').center(self.terminal_width))
        print((f'{Colors.FAIL}          #        #      #  #   #   #  #   #   #  ########  #            #      #   #{Colors.ENDC}    ').center(self.terminal_width))
        print((f'{Colors.FAIL}          #        #      #  #    #  #  #    #  #  #         #            #      ########{Colors.ENDC} ').center(self.terminal_width))
        print((f'{Colors.FAIL}          #        #      #  #      ##  #      ##  #         #            #          #{Colors.ENDC}    ').center(self.terminal_width))
        print((f'{Colors.FAIL}          #######  ########  #       #  #       #  ########  ########     #          #{Colors.ENDC}    ').center(self.terminal_width))
        print('')
        print((f'{Colors.FAIL}          #*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#{Colors.ENDC}').center(self.terminal_width))
        print((f'{Colors.FAIL}                                  Connect4 by {Colors.WARNING}nhee{Colors.FAIL}            {Colors.ENDC}').center(self.terminal_width))
        print((f'{Colors.FAIL}          #*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#{Colors.ENDC}').center(self.terminal_width))

    def start_screen(self):
        print('')
        print((f'{Colors.FAIL}         ##################################################################################{Colors.ENDC}').center(self.terminal_width))
        print((f'                                 {Colors.WARNING}[1] Player vs. Player                 {Colors.ENDC}').center(self.terminal_width))
        print((f'                                 {Colors.WARNING}[2] Player vs. Computer               {Colors.ENDC}').center(self.terminal_width))
        print((f'                    {Colors.WARNING}[3] Computer vs. Computer{Colors.ENDC}').center(self.terminal_width))
        print((f'      {Colors.WARNING}[4] Options{Colors.ENDC}').center(self.terminal_width))
        print((f'    {Colors.WARNING}[5] Exit{Colors.ENDC}').center(self.terminal_width))
        print((f'{Colors.FAIL}         ##################################################################################{Colors.ENDC}').center(self.terminal_width))
        print('')

    def enter_help(self):
        print((f'{Colors.FAIL}                                    {Colors.WARNING}Use the Help{Colors.FAIL}              {Colors.ENDC}').center(self.terminal_width))
        print((f'{Colors.FAIL}          #*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#{Colors.ENDC}').center(self.terminal_width))

    def options_screen(self):
        print('')
        print((f'{Colors.FAIL}         ##################################################################################{Colors.ENDC}').center(self.terminal_width))
        print((f'                {Colors.WARNING}[1] Change board size{Colors.ENDC}').center(self.terminal_width))
        print((f'            {Colors.WARNING}[2] Back to start{Colors.ENDC}').center(self.terminal_width))
        print((f'{Colors.FAIL}         ##################################################################################{Colors.ENDC}').center(self.terminal_width))
        print('')

    def option_change_gameboard(self, rows, columns):
        print('')
        print((f'{Colors.FAIL}         ##################################################################################{Colors.ENDC}').center(self.terminal_width))
        print((f'          {Colors.WARNING}Enter row and column size{Colors.ENDC}').center(self.terminal_width))
        print('')
        print((f'{Colors.WARNING}Default:{Colors.ENDC}       ').center(self.terminal_width))
        print((f'{Colors.WARNING}Rows: {rows}{Colors.ENDC}        ').center(self.terminal_width))
        print((f'{Colors.WARNING}Columns: {columns}{Colors.ENDC}     ').center(self.terminal_width))
        print((f'{Colors.FAIL}         ##################################################################################{Colors.ENDC}').center(self.terminal_width))
        print('')

    def show_help(self):
        print('')
        print('')
        print((f'{Colors.FAIL}         ##################################################################################{Colors.ENDC}').center(self.terminal_width))
        print('')
        print((f'{Colors.WARNING}Enter one of the following letters{Colors.ENDC}').center(self.terminal_width))
        print((f'{Colors.WARNING}b : BACK TO START SCREEN{Colors.ENDC}').center(self.terminal_width))
        print((f'{Colors.WARNING}e : EXIT{Colors.ENDC}').center(self.terminal_width))
        print('')
        print((f'{Colors.FAIL}         ##################################################################################{Colors.ENDC}').center(self.terminal_width))
        print('')
        print('')

    def winning_player(self, player):
        print('')
        print('')
        print('###################################')
        print('')
        print('############ {} wins! #############'.format(player.name))
        print('')
        print('###################################')
        print('')
        print('')

    def clear_console(self):
        os.system('cls')

    def init_game_mode(self):
        game_mode = input('Enter Option: ')
        return game_mode

    def player_input(self, name):
        player_input = input('{} drop your chip(1-7): '.format(name))
        reg_ex = re.search('[1-7]', player_input)

        if player_input.lower() == 'help':
            self.clear_console()
            self.connect_four()
            self.show_help()
        elif player_input.lower() == 'b' or player_input.lower() == 'e':
            return player_input
        elif reg_ex and len(player_input) == 1:
            return int(player_input)
        else:
            self.show_message('invalid input')

    def show_board(self, columns, rows, board):
        column_index_string = ''
        separator_string = ''

        print('')
        for row in range(rows):
            row_string = ''
            for column in range(columns):
                if board.board[row][column] == 0:
                    row_string += '[ ]'
                elif board.board[row][column] == 1:
                    row_string += '[X]'
                elif board.board[row][column] == 2:
                    row_string += '[O]'

                if row == 0:
                    column_index_string += '|' + str((column +1)) + '|'
            print(row_string.center(self.terminal_width))
        
        for _ in range(len(column_index_string)):
            separator_string += '_'

        print(separator_string.center(self.terminal_width))
        print(column_index_string.center(self.terminal_width))
        print('')

    def show_message(self, message):
        print(message)