n = int(input())
name = []
height = []
weight = []

class person:
    def __init__(self, name, height, weight):
        self.n=name
        self.h=height
        self.w=weight
    
people=[]
for _ in range(n):
    n_i, h_i, w_i = input().split()
    people.append(person(n_i, h_i, w_i))

# Please write your code here.
people.sort(lambda x: x.h)
for i in range(n):
    print(people[i].n, people[i].h, people[i].w)