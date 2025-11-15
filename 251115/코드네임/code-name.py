MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.

class men:
    def __init__ (self, name="none", score=0):
        self.name=name
        self.score=score
mens= []
for i in range(5):
    name = codenames[i]
    score = scores[i]
    mens.append(men(name, score))

min=1000
min_index=0
for i in range(5):
    if min>mens[i].score:
        min=mens[i].score
        min_index=i

print(mens[min_index].name, mens[min_index].score)