from itertools import product
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = [a,b]
for i in product(*ans):
    print(i ,end=' ')
'''
from itertools import product
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(*product(a, b))
'''