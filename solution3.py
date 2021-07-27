s='b'+''.join(format(ord(c),'07b') for c in input());r=''
for i,b in enumerate(s[1:]):r+=' '+'00 0'[int(b):] if not b==s[i] else '0'
print(r[1:])
