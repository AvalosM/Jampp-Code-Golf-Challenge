i=''.join(format(ord(c),'07b') for c in input());c=0;r='';l=i[0]
for b in i:
	if b==l:c+=1
	else:r+='0'*-(int(l)-2)+' '+'0'*c+' ';c=1;l=b
r+='0'*-(int(l)-2)+' '+'0'*c;print(r)

print(r)
