n=int(input())
w=len("{0:b}".format(n))
for i in range(1,n+1) :
	d=str(i)
	b=str("{0:b}".format(i))
	o=str("{0:o}".format(i))
	h="{0:x}".format(i)
	h=str(h).upper()
	print(d.rjust(w),b.rjust(w),o.rjust(w),h.rjust(w))

