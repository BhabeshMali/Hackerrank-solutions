n = int(input())
s = set(map(int, input().split()))
m=int(input())
for i in range(m) :
	u=list(map(str,input().split()))
	if u[0]=="pop" :
		s.pop()
	if u[0]=="remove" :
		k=int(u[1])
		s.remove(k)
	if u[0]=="discard" :
		k=int(u[1])
		s.discard(k)
s=str(list(s))
print(s.replace('[','').replace(']',''))
