#week10_06.py

class Score:
    def __init__(self, k, m, e): #magic method
        self.kor = k
        self.mat = m
        self.eng = e

    def average(self): #method
        return (self.kor + self.mat + self.eng) / 3

score3 = Score(10,20,30)
print(score3.kor, score3.mat)
print(score3.average())

score3.kor = 100
print(score3.kor, score3.mat)
print(score3.average())


scores1 = [10, 20, 30]
scores2 = {"k":10, "e":20, "m":30}

def average_list(datas):
    return sum(datas)/len(datas)

def average_dict(datas):
    return sum(datas.values())/len(datas)

print(average_list(scores1))
print(average_dict(scores2))

