n = int(input())
t=list()
o=input().split()
for i in range(n) :
	p=int(o[i])
	t.append(p)
tup=tuple(t)
print(hash(tup))
