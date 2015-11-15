
class Score:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
class HighScore:
    def __init__(self):
        f = open("score", "r")
        
        self.scores = []

        for line in f:
            segments = line.split("`")
            
            self.scores.append(Score(segments[0], int(segments[1][:-1])))

        self.sort()

    def addScore(self, name, score):
        self.scores.append(Score(name, score))

        self.sort()


    def printScore(self):
        for i in range(0, min(10, len(self.scores))):
            print "{}: {}".format(self.scores[i].name, self.scores[i].score)

    def getString(self):
        result = ""

        for i in range(0, min(10, len(self.scores))):
            result = ("{}{}: {}\n".format(result, self.scores[i].name, self.scores[i].score))
        return result

    def sort(self):
        self.scores.sort(key = lambda score: score.score, reverse=True)

    def getLowest(self):
        if(len(self.scores) != 0):
            index = min(9, len(self.scores) - 1)
            return self.scores[index].score
        else:
            return 0

    def save(self):
        f = open("score", "w")

        for i in range(0, min(10, len(self.scores))):
            f.write("{}`{}\n".format(self.scores[i].name, self.scores[i].score))
