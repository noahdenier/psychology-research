class Competitor:
    def __init__(self, gamertag, gender):
        self.gamertag = gamertag
        self.gender = gender
        self.wins = 0
        self.losses = 0

    def increment_w_l(self,result):
        if result is 'W':
            self.wins += 1
        if result is 'L':
            self.losses += 1
