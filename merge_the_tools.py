from collections import OrderedDict
string, k = input(),int(input())
lngt=len(string)
sub_len=int(lngt/k)
sub_str=[]
for i in range(0,lngt,k) :
	st=(string[i:i+k])
	sub_str.append("".join(OrderedDict.fromkeys(st)))
print((" ".join(sub_str)).replace(" ","\n"))

