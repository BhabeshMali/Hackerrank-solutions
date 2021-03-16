n=int(input())
alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(n) :
	if i<(n-1/2) :
		pattern=alp[n]
		print((pattern*(2*i+1)).center(n,"-"))


