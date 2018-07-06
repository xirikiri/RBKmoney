import random
import time
start_time = time.time()
"""
5 procentov veroyatnosti oshibitsya
"""

def little_random(input):
    if (input == "fair"):
        return random.choices([input, "scam"], weights=[95,5]).pop()
    if (input == "scam"):
        return random.choices([input, "fair"], weights=[95,5]).pop()

"""
Traders Class Declaratioin
"""

class Altruist():
    def __init__(self):
        self.strategy = "altruist"
        self.profit = 0
        self.opponent_history = []
    def request(self):
        return [self, little_random("fair")]

class Kidala():
    def __init__(self):
        self.strategy = "kidala"
        self.profit = 0
        self.opponent_history = []
    def request(self):
        return [self, little_random("scam")]

class Hitrez():
    def __init__(self):
        self.strategy = "Hitrez"
        self.profit = 0
        self.opponent_history = []
    def request(self):
        if len(self.opponent_history) == 0:
            return [self, little_random("fair")]
        return [self, little_random(self.opponent_history[-1])]

class Nepredskazuemy():
    def __init__(self):
        self.strategy = "Nepredskazuemy"
        self.profit = 0
        self.opponent_history = []
    def request(self):
        return [self, little_random(random.choices(["fair", "scam"], weights=[1,1]).pop())]

class Zlopamatny():
    def __init__(self):
        self.strategy = "Zlopamatny"
        self.profit = 0
        self.opponent_history = []
    def request(self):
        if len(self.opponent_history) == 0:
            return [self, little_random("fair")]
        if "scam" in self.opponent_history:
            return [self, little_random("scam")]
        return [self, little_random("fair")]

class New():
    def __init__(self):
        self.strategy = "new"
        self.profit = 0
        self.opponent_history = []
    def request(self):
        if len(self.opponent_history) == 0:
            return [self, little_random("fair")]
        if len(self.opponent_history) == 1:
            return [self, little_random("fair")]
        if "scam" in self.opponent_history:
            return [self, little_random("scam")]
        return [self, little_random("fair")]

class Ushly():
    def __init__(self):
        self.strategy = "Ushly"
        self.profit = 0
        self.opponent_history = []
    def request(self):
        if len(self.opponent_history) == 1:
            return [self, little_random("scam")]
        if len(self.opponent_history) < 5:
            return [self, little_random("fair")]
        if "scam" in self.opponent_history[0-4]:
            return [self, little_random("scam")]
        else:
            if len(self.opponent_history) == 5:
                return [self, little_random("fair")]
            else:
                return [self, little_random(self.opponent_history[-1])]

"""
Deal processing
"""

def deal(request_1, request_2):
    #print(request_1, request_2)
    if (request_1[1] == "fair") and (request_2[1] == "fair"):
        request_1[0].profit += 4
        request_2[0].profit += 4
    if (request_1[1] == "scam") and (request_2[1] == "scam"):
        request_1[0].profit += 2
        request_2[0].profit += 2
    if (request_1[1] == "scam") and (request_2[1] == "fair"):
        request_1[0].profit += 5
        request_2[0].profit += 1
    if (request_1[1] == "fair") and (request_2[1] == "scam"):
        request_1[0].profit += 1
        request_2[0].profit += 5
    request_1[0].opponent_history.append(request_2[1])
    request_2[0].opponent_history.append(request_1[1])
"""
1 year Deal
"""

def year_deal(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1, i, -1):
            for count in range(random.choices([5,6,7,8,9,10], weights=[1,1,1,1,1,1]).pop()):
                deal(arr[i].request(),arr[j].request())
            arr[i].opponent_history = []
            arr[j].opponent_history = []
"""
bubble_sort
"""

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j].profit > arr[j-1].profit:
                arr[j], arr[j-1] = arr[j-1], arr[j]


def evolution(Guild):
    temp_strategy_array = []
    while (len(temp_strategy_array) != 1):
        temp_strategy_array = []
        year_deal(Guild)
        bubble_sort(Guild)
        for i in range(12):
            Guild.pop()
        for i in range(12):
            if (Guild[i].strategy == "altruist"):
                Guild.append(Altruist())
            if (Guild[i].strategy == "kidala"):
                Guild.append(Kidala())
            if (Guild[i].strategy == "Hitrez"):
                Guild.append(Hitrez())
            if (Guild[i].strategy == "Nepredskazuemy"):
                Guild.append(Nepredskazuemy())
            if (Guild[i].strategy == "Zlopamatny"):
                Guild.append(Zlopamatny())
            if (Guild[i].strategy == "Ushly"):
                Guild.append(Ushly())
            if (Guild[i].strategy == "new"):
                Guild.append(New())

        for i in Guild:
            i.profit = 0
            temp_strategy_array.append(i.strategy)
        temp_strategy_array = list(set(temp_strategy_array))
    return temp_strategy_array.pop()
"""
Main function
"""

if __name__ == "__main__":
    result = []
    for i in range(100):
        Guild = []
        for i in range(10):
            Guild.append(Altruist())
            Guild.append(Kidala())
            Guild.append(Hitrez())
            Guild.append(Nepredskazuemy())
            Guild.append(Zlopamatny())
            Guild.append(Ushly())
            Guild.append(New())
        result.append(evolution(Guild)
    print(result)
    print("--- %s seconds ---" % (time.time() - start_time))
