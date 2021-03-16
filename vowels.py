s=input()
k=int(input().strip())
for o in range(len(s)) :
	q.append(s[o:k])
	k=k+1
	if k>s :
		break

p='aeiou'
l=[]
for i in p :
	l.append(i)
	for m in range(len(q)) :
		for h in q[m] :
			if i==h :
				sum=sum+1
		
		

