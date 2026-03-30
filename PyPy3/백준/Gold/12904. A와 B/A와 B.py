start=list(input())
end=list(input())

# end에서 start를 만들자
# 1. 뒤에 A를 뺀다
# 2. 뒤에 B를 버리고 뒤집는다

while len(start)<len(end):
    if end[-1]=='A':
        end=end[:-1]
    else:
        end=end[:-1]
        end=end[::-1]

if start==end:
    print(1)
else:
    print(0)