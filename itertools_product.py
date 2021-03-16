from itertools import product
l=list(map(int,input().split()))
j=list(map(int,input().split()))
k=(list(product(l,j)))
print(" ".join("(" +str(a)+", "+str(b)+")" for a,b in k))
