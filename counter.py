from collections import Counter
p=input()
o=list(map(int,input().split()))
t=(Counter(o))
m=list(t.keys())
n=list(t.values())
no=int(input())
sum=0
for i in range(no) :
	u,k = list(map(int,input().split()))
	if t[u]>0 :
		print(t[u])
		sum=sum+k
		t[u]=t[u]-1
print(sum)
