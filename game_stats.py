class GameStats:

    def __init__(self):
        self.pac_lives = 3
        self.points = 0

    def reset_stats(self):
        self.points = 0
        self.pac_lives = 3