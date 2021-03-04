a = []
n = int(input())    # stroka
m = int(input())    # stolbec
for i in range(n):
    b = []
    for j in range(m):
        b.append(int(input()))
    a.append(b)
for i in a:
    print(i)
