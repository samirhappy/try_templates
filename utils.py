import json


class Candidate:
    def __init__(self, path):
        self.path = path

    def load_candidates_in_dict(self):
        candidate = {}
        with open(self.path, 'r') as file:
            data = json.load(file)
        for i in data:
            candidate[i['id']] = i
        return candidate

    def get_data_from_id(self, id1):
        candidate = {}
        with open(self.path, 'r') as file:
            data = json.load(file)
        for i in data:
            candidate[i['id']] = i
        return candidate[int(id1)]

    def get_candidates_by_name(self, candidate_name):
        candidate = {}
        count = 1
        string = {}
        with open(self.path, 'r') as file:
            data = json.load(file)
        for i in data:
            candidate[i['id']] = i
        for can_ in candidate.values():
            candidate1 = can_['name'].split(' ')
            if candidate_name in candidate1:
                string[count] = can_['name']
            count += 1
        return string

    def get_candidates_by_skill(self, skill_name):
        candidate = {}
        count = 1
        string = {}
        with open(self.path, 'r') as file:
            data = json.load(file)
        for i in data:
            candidate[i['id']] = i
        for can_ in candidate.values():
            candidate1 = can_['skills'].split(', ')
            candidate1 = [x.lower() for x in candidate1]
            if skill_name in candidate1:
                string[count] = can_['name']
        return string


cla = Candidate('candidate.json')
# print(cla.load_candidates_in_dict())
# print(cla.get_candidates_by_skill('python'))
print(cla.get_candidates_by_name('Austin'))
