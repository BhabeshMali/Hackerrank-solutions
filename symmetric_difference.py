r1=int(input())
o=list(map(int,input().split()))
o=set(o)
r2=int(input())
p=list(map(int,input().split()))
p=set(p)
l=len(o.symmetric_difference(p))
print(l)
