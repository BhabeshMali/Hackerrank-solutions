o=input()
sub_str=input()
count=0
for i in range(len(o)) :
	if o[i:].startswith(sub_str) :
		count=count+1
print(count)
