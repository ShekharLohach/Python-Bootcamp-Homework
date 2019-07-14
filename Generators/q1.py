def gensquare(n):
    for i in range(n):
        yield pow(i,2)

for i in gensquare(4):
    print(i)

