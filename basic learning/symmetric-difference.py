input()
a = set(map(int,input().split()))
input()
b = set(map(int,input().split()))
c = a.symmetric_difference(b)
c = list(c)
c.sort()
for i in c:
    print (i)