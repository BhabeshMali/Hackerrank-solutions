n=input("Enter the number of operation\n")
l=[]
for _ in range(int(n)) :
	op = input().split()
	try :
		n1=int(op[1])
	except :
		n1=0
	try :
		n2=int(op[2])
	except :
		n2=0
	if op[0]=="insert" :
		l.insert(n1,n2)
	if op[0]=="append" :
		l.append(n1)
	if op[0]=="remove" :
		l.remove(n1)
	if op[0]=="sort" :
		l.sort()
	if op[0]=="print" :
		print(l)
	if  op[0]=="pop" :
		l.pop()
	if op[0]=="reverse" :
		l.reverse()
