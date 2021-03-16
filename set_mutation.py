u=int(input())
o=set(map(int,input().split()))
p=int(input())
for i in range(p) :
    l,m=list(map(str,input().split()))
    m=int(m)
    k=set(map(int,input().split()))
    if l=="intersection_update" :
        o.intersection_update(k)
    if l=="update" :
        o.update(k)
    if l=="symmetric_difference_update" :
        o.symmetric_difference_update(k)   
    if l=="difference_update" :
        o.difference_update(k)
print(sum(list(o)))
