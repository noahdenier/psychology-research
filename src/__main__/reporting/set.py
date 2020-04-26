from .competitor import Competitor
import json

with open('path_to_file/person.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data)

class Set:
    def __init__(player_1_results, player_2_results):
        self.player_1_results = player_1_results
        self.player_2_results = player_2_results

    def report_sets(self):
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
