n,m=map(int,input().split(" "))
for i in range(n) :
	pattern = '.|.'
	if i<(n-1)/2 :
		print((pattern*(2*i+1)).center(m,"-"))
	elif i==(n-1)/2 :
		print("Welcome".center(m,"-"))
	else :
		print((pattern*(2*(n-1-i)+1)).center(m,"-"))
