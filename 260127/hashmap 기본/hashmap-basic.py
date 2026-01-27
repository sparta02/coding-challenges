n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))

# Please write your code here.

hashmap={}

for com in commands:
    if com[0]=='add':
        hashmap[com[1]]=com[2]
    elif com[0]=='remove':
        hashmap.pop(com[1])
    else:
        print(hashmap.get(com[1], "None"))
