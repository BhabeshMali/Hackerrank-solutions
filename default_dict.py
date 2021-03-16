from collections import defaultdict
d=defaultdict(list)
n,m = map(int,input().split())
l=[]
for i in range(1,n+1) :
	p=input()
	d[i].append(p)
for j in range(1,m+1) :
	q=input()
	l.append(q)
y=[]
w=[]
for k in range(0,m) :
	for ii,jj in d.items() :
		t=''.join(jj)
		if l[k]==t :
			y.append(ii)
	if not y:
		print('-1')
	else :
		print((str(y)[1:-1]).replace(",",""))
	y.clear()
