n=int(input())
for _ in range(n):
    num=int(input())
    if (num+1)%(num%100)==0:
        print('Good')
    else:
        print('Bye')