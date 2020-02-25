class Player:
    
    def __init__(self, chip_id, name):
        self.chip_id = chip_id
        self.name = name
        self.type = 'human'
        self.active = False