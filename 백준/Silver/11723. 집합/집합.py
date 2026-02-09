import sys
input = sys.stdin.readline

n=int(input())
S=0

for _ in range(n):
    commands=list(input().split())
    if commands[0]!='all' and commands[0]!='empty':
        commands[1]=int(commands[1])
    
    if commands[0]=='add':
        S=S|(1<<commands[1])
    elif commands[0]=='remove':
        S= S&~(1<<commands[1])
    elif commands[0]=='check':
        print(1 if S&(1<<commands[1]) else 0)
    elif commands[0]=='toggle':
        S=S^(1<<commands[1])
    elif commands[0]=='all':
        S=(1<<21)-1
    elif commands[0]=='empty':
        S=0


    
    