#o=input()
#kcount=0
#scount=0
#sub_str=[]
#y=[]
#w=[]
#for j in range(1,len(o)+1) :
#for i in range(len(o)) :
#	if o[i]=="A" or o[i]=="E" or o[i]=="I" or o[i]=="O" or o[i]=="U" :
#		y.append(i)
#	else :
#		w.append(i)
#print(y)
#print(w)
#u=[]
#s=[]
#for m in range(len(y)) :
#	for j in range(len(o)+1) :
#		if m+1<j :
#			st=o[y[m]:j]
#			if len(st)<1 :
#				continue
#			else :
#				kcount=kcount+1

#print(kcount)
#while ("" in s) :
#	s.remove("")
#print(s)
#print(len(s))
#for i in range(len(w)) :
#	for j in range(len(o)+1) :
#		if i<j :
#			st=o[w[i]:j]
#			if len(st)<1 :
#				continue
#			else :
#				scount=scount+1
#print(scount)
#while ("" in u) :
#	u.remove("")
#print(u)
#if len(s)>len(u) :
#	print("KEVIN"+" "+str(len(s)))
#elif len(s)==len(u) :
#	print("DRAW")
#else :
#	print("STUART"+" "+str(len(u)))

o=input("Enter the String\n")
kcount=0
scount=0
s="AEIOU"
for i in range(len(o)) :
        if o[i] in s :
                kcount+=(len(o)-i)
                #print(kcount)
        else :
                scount+=(len(o)-i)
                #print(scount)
if kcount>scount :
        print("Kevin"+" "+str(kcount))
elif kcount==scount :
        print("Draw")
else :
        print("Stuart"+" "+str(scount))

