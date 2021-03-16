from itertools import permutations
o=list(map(str,input().split()))
s=o[0]
l=int(o[1])
k=list(permutations(s,l))
k.sort()
for i in range(len(k)) :
    k[i]=''.join(k[i])
    print(k[i])
