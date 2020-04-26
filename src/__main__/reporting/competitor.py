class Competitor:
    def __init__(self, gamertag, gender):
        self.gamertag = gamertag
        self.gender = gender
        self.set_history = {}

    def init_event(self, event):
        self.set_history[event] = {
            'W':0,
            'L':0
            }

    def increment_w_l(self,event,result):
        if result is 'W':
            self.set_history[event]['W'] += 1
        if result is 'L':
            self.set_history[event]['L'] += 1

    def report_set(self, event, result):
        if event not in self.set_history:
            self.init_event(event)
        self.increment_w_l(event, result)

    # def lookup_gender(self):
    #
