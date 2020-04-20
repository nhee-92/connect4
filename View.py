import re
import os

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
        print((f'                                 {Colors.WARNING}(1) Player vs. Player                 {Colors.ENDC}').center(self.terminal_width))
        print((f'                                 {Colors.WARNING}(2) Player vs. Computer               {Colors.ENDC}').center(self.terminal_width))
        print((f'                    {Colors.WARNING}(3) Computer vs. Computer{Colors.ENDC}').center(self.terminal_width))
        print((f'      {Colors.WARNING}(4) Options{Colors.ENDC}').center(self.terminal_width))
        print((f'    {Colors.WARNING}(5) Exit{Colors.ENDC}').center(self.terminal_width))
        print((f'{Colors.FAIL}         ##################################################################################{Colors.ENDC}').center(self.terminal_width))
        print('')

    def enter_help(self):
        print((f'{Colors.FAIL}                                    {Colors.WARNING}Use the Help{Colors.FAIL}              {Colors.ENDC}').center(self.terminal_width))
        print((f'{Colors.FAIL}          #*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#{Colors.ENDC}').center(self.terminal_width))

    def options_screen(self):
        print('')
        print((f'{Colors.FAIL}         ##################################################################################{Colors.ENDC}').center(self.terminal_width))
        print((f'                {Colors.WARNING}(1) Change board size{Colors.ENDC}').center(self.terminal_width))
        print((f'            {Colors.WARNING}(2) Back to start{Colors.ENDC}').center(self.terminal_width))
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
        print((f'{Colors.WARNING}n : NEW GAME{Colors.ENDC}').center(self.terminal_width))
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
        elif player_input.lower() == 'b' or player_input.lower() == 'n' or player_input.lower() == 'e':
            return player_input
        elif reg_ex and len(player_input) == 1:
            return int(player_input)
        else:
            self.show_message('invalid input')

    def show_board(self, columns, rows, board, players):
        visual_game_board = ''

        for column in range(columns):
            for row in range(rows):
                if board.board[row][column] == 0:
                    visual_game_board += '[ ]'
                elif board.board[row][column] == 1:
                    visual_game_board += '[X]'
                elif board.board[row][column] == 2:
                    visual_game_board += '[O]'

        print('')
        print((visual_game_board[0:3] + visual_game_board[18:21] + visual_game_board[36:39] + visual_game_board[54:57] + visual_game_board[72:75] + visual_game_board[90:93] + visual_game_board[108:111]).center(self.terminal_width))
        print((visual_game_board[3:6] + visual_game_board[21:24] + visual_game_board[39:42] + visual_game_board[57:60] + visual_game_board[75:78] + visual_game_board[93:96] + visual_game_board[111:114]).center(self.terminal_width))
        print((visual_game_board[6:9] + visual_game_board[24:27] + visual_game_board[42:45] + visual_game_board[60:63] + visual_game_board[78:81] + visual_game_board[96:99] + visual_game_board[114:117]).center(self.terminal_width))
        print((visual_game_board[9:12] + visual_game_board[27:30] + visual_game_board[45:48] + visual_game_board[63:66] + visual_game_board[81:84] + visual_game_board[99:102] + visual_game_board[117:120]).center(self.terminal_width))
        print((visual_game_board[12:15] + visual_game_board[30:33] + visual_game_board[48:51] + visual_game_board[66:69] + visual_game_board[84:87] + visual_game_board[102:105] + visual_game_board[120:123]).center(self.terminal_width))
        print((visual_game_board[15:18] + visual_game_board[33:36] + visual_game_board[51:54] + visual_game_board[69:72] + visual_game_board[87:90] + visual_game_board[105:108] + visual_game_board[123:126]).center(self.terminal_width))
        print('_____________________'.center(self.terminal_width))
        print('|1||2||3||4||5||6||7|'.center(self.terminal_width))
        print('')

    def show_message(self, message):
        print(message)