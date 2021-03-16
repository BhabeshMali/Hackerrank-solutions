o=int(input())
s=[]
ad={'1'}
for i in range(o) :
	p=input()
	s.append(p)
for j in s :
	j="".join(j)
	ad.add(j)
print(len(ad)-1)
