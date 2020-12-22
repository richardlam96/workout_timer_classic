

class TimeConfiguration(object):

    def __init__(self, work=0, rest=0, rounds=0, round_rest=0):
        self.work = int(work)
        self.rest = int(rest)
        self.rounds = int(rounds)
        self.round_rest = int(round_rest)

