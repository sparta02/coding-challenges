n = int(input())
commands = []
x = []
for _ in range(n):
    cmd, val = input().split()
    commands.append(cmd)
    x.append(int(val))

hash=set()

for com, num in zip(commands, x):
    if com=='add':
        hash.add(num)
    elif com=='remove':
        hash.remove(num)
    else:
        print('true' if num in hash else 'false')
