import re
e=re.compile(r'([0-1])\1*')
s=e.finditer(''.join(format(ord(c),'07b') for c in input()))
r=''
for m in s:r+='00 '[int(m[0][0]):]+'0'*len(m[0]) +' '
print(r)
