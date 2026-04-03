temp=[ list(input().split()) for _ in range(3)]
persons=[]
for a,b,c in temp:
    persons.append((int(a), int(b), c))
# print(persons)

one=[]
for a,b,c in persons:
    one.append(b%100)
one.sort()

for i in one:
    print(i, end="")
print()

two=[]
for a,b,c in persons:
    two.append((a,c[0]))
two.sort(reverse= True)

for i,j in two:
    print(j, end="")
print()
