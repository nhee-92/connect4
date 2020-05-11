import random

class Ai:

    ################
    ### AI Names ###
    ai_names = [
        'Darth Vader',
        'Luke Skywalker',
        'R2D2',
        'Obiwan Kenobi',
        'C3PO',
        'Anakin Skywalker',
        'Master Yoda',
        'Qui-Gon Jinn',
        'Darth Maul',
        'Darth Sidious'
    ]
    
    def __init__(self, chip_id):
        self.chip_id = chip_id
        self.name = self.pick_ai_name()
        self.type = 'machine'
        self.active = False

    def pick_ai_name(self):
        return random.choice(self.ai_names)