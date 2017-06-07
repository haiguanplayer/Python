a = []
n = int(input())
while (n > 0):
    n -= 1;
    s = input().strip().split(" ")
    if s[0] == "insert":
        i = int(s[1]);val = int(s[2]);
        a.insert(i, val);
    elif s[0] == "sort":
        a.sort();
    elif s[0] == "remove":
        val = int(s[1]);
        a.remove(val)
    elif s[0] == "reverse":
        a.reverse();
    elif s[0] == "append":
        val = int(s[1])
        a.append(val);
    elif s[0] == "pop":
        a.pop();
    else:
        print (a)
'''
n = input()
l = []
for _ in range(n):
    s = raw_input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print l
'''
