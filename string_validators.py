l=[]
o=input()
for i in o :
	t=i.split()
	l.append(t)
s=[]
a=[]
b=[]
c=[]
d=[]
for i in range(len(l)) :
	check=''.join(l[i])
	t1=check.isalpha()
	s.append(t1)
	t2=check.isalnum()
	a.append(t2)
	t3=check.isdigit()
	b.append(t3)
	t4=check.islower()
	c.append(t4)
	t5=check.isupper()
	d.append(t5)
if True in a :
	print('True')
else : print('False')
if True in s :
	print('True')
else : print('False')
if True in b :
        print('True')
else : print('False')
if True in c :
        print('True')
else : print('False')
if True in d :
        print('True')
else : print('False')
