q = int(input())
commands = []
for _ in range(q):
    line = input().split()
    if line[0] != "clear":
        commands.append((line[0], int(line[1])))
    else:
        commands.append((line[0],))

S=0
for line in commands:
    if line[0]=='clear':
        S=0
    elif line[0]=='add':
        S|=(1<<line[1])
    elif line[0]=='print':
        if S&1<<line[1]:
            print(1)
        else:
            print(0)
    elif line[0]=='toggle':
        S^=(1<<line[1])
    elif line[0]=='delete':
        S&=~(1<<line[1])

