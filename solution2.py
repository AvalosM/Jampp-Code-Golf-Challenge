import re;r=''
for m in re.compile(r'([0-1])\1*').finditer(''.join(format(ord(c),'07b') for c in input())):r+='00 '[int(m[0][0]):]+'0'*len(m[0]) +' '
print(r)
