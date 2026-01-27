n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code
words = [input() for _ in range(n)]
queries = [input() for _ in range(m)]

# Please write your code here.

maps={}
for i, word in enumerate(words):
    maps[str(i+1)]=word
    maps[word]=str(i+1)
# print(maps)

for q in queries:
    print(maps[str(q)])