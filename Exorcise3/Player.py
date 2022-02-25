class Player:
    def __init__(self, name, num, batted, hits, double, triple, homeruns):
        self.name = name
        self.num = num
        self.batted = batted
        self.hits = hits
        self.double = double
        self.triple = triple
        self.homeruns = homeruns
        self.average = self.hits + self.double + self.triple + self.homeruns / 4

    def __str__(self):
        return "name: {}, num: {}, batted: {}, hits: {}, double: {}, triple: {}, homeruns: {}, average: {}" \
            .format(self.name, self.num, self.batted, self.hits, self.double, self.triple, self.homeruns, self.average)
