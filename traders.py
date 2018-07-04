import random

"""
Traders Class Declaratioin
"""

class Trader:
    def __init__(self):
        self.profit = 0
        self.opponent_history = []

class Altruist(Trader):
    def __init__(self):
        self.strategy = "altruist"
    def request(self):
        return [self, "fair"]

class Kidala(Trader):
    def __init__(self):
        self.strategy = "kidala"
    def request(self):
        return [self, "scam"]

class Hitrez(Trader):
    def __init__(self):
        self.strategy = "Hitrez"
    def request(self):
        if len(self.opponent_history) == 0:
            return [self, "fair"]
        return [self, self.opponent_history[-1]]

class Nepredskazuemy(Trader):
    def __init__(self):
        self.strategy = "Nepredskazuemy"
    def request(self):
        return [self, random.choices(["fair", "scam"], weights=[1,1])]

class Zlopamatny(Trader):
    def __init__(self):
        self.strategy = "Zlopamatny"
    def request(self):
        if len(self.opponent_history) == 0:
            return [self, "fair"]
        if "scam" in self.opponent_history:
            return [self, "scam"]

class Ushly(Trader):
    def __init__(self):
        self.strategy = "Ushly"
    def request(self):
        if len(self.opponent_history) == 1:
            return [self, "scam"]
        if len(self.opponent_history) < 5:
            return [self, "fair"]
        if "scam" in self.opponent_history[0-4]:
            return [self, "scam"]
        else:
            if len(self.opponent_history == 5):
                return [self, "fair"]
            else:
                return [self, self.opponent_history[-1]]

"""
Deal processing
"""

def deal(request_1, request_2):
    if (request_1[1] == "fair") and (request_2[1] == "fair"):
        request_1[0].profit += 4
        request_2[0].profit += 4
    if (request_1[1] == "scam") and (request_2[1] == "scam"):
        request_1[0].profit += 2
        request_2[0].profit += 2
    if (request_1[1].action == "scam") and (request_2[1] == "fair"):
        request_1[0].profit += 5
        request_2[0].profit += 1
    if (request_1[1] == "fair") and (request_2[1] == "scam"):
        request_1[0].profit += 1
        request_2[0].profit += 5
    request_1[0].opponent_history.append(request_2[1])
    request_2[0].opponent_history.append(request_1[1])

"""
Main function
"""

if __name__ == "__main__":
    Guild = []
    for i in range(10):
        Guild.append(Altruist())
        Guild.append(Kidala())
        Guild.append(Hitrez())
        Guild.append(Nepredskazuemy())
        Guild.append(Zlopamatny())
        Guild.append(Ushly())
    print(len(Guild))
    for i in Guild:
        
