n,m = list(map(int,input().split()))
o = list(map(int,input().split()))
a = list(map(int,input().split()))
a=set(a)
b = list(map(int,input().split()))
b=set(b)
l=0
for i in range(n) :
    if o[i] in a:
        l=l+1
    if o[i] in b:
        l=l-1
print(l)
