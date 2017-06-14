from itertools import permutations
s,n = input().split(" ")
perm = list(permutations(s,int(n)))
perm.sort()
for i in perm:
    print ("".join(i))
