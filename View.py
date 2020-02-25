import re

class View:

    def start_screen(self):
        print('')
        print('          #######  ########  #       #  #       #  ########  ########  ########  #')
        print('          #        #      #  # #     #  # #     #  #         #            #      #')
        print('          #        #      #  #  #    #  #  #    #  #         #            #      #   #')
        print('          #        #      #  #   #   #  #   #   #  ########  #            #      #   #')
        print('          #        #      #  #    #  #  #    #  #  #         #            #      ########')
        print('          #        #      #  #      ##  #      ##  #         #            #          #')
        print('          #######  ########  #       #  #       #  ########  ########     #          #')
        print('')
        print('          #*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#')
        print('          #                             Connect4 by nhee                                  #')
        print('          #*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#')
        print('')
        print('#####################################################################################################')
        print('######### (1) Player vs. Player ### (2) Player vs. Computer ### (3) Computer vs. Computer ###########')
        print('############################################# (4) Exit ##############################################')
        print('')

    def show_help(self):
        print('')
        print('')
        print('############## Help ###############')
        print('')
        print('Enter one of the following letters')
        print('b : BACK TO START SCREEN')
        print('n : NEW GAME')
        print('e : EXIT')
        print('')
        print('###################################')
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

    def init_game_mode(self):
        game_mode = input('Enter Option: ')
        return game_mode

    def player_input(self, name):
        player_input = input('{} drop your chip(1-7) or enter help: '.format(name))
        reg_ex = re.search('[1-7]', player_input)

        if player_input.lower() == 'help':
            self.show_help()
        elif player_input.lower() == 'b' or player_input.lower() == 'n' or player_input.lower() == 'e':
            return player_input
        elif reg_ex and len(player_input) == 1:
            return int(player_input)
        else:
            self.show_message('invalid input')

    def show_board(self, board):
        print(board)

    def show_message(self, message):
        print(message)